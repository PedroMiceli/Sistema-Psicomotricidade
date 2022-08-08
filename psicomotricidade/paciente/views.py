from django.template.loader import get_template
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .utils import *
from .relatorio import relatorio as relatorio_textos
from .dataframes import unidades_funcionais as unidades
from xhtml2pdf import pisa


# ------------------------- PACIENTE -------------------------
class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome', 'data_nascimento', 'responsavel', 'cpf_responsavel']
    template_name = 'paciente/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(PacienteCreate, self).get_form(form_class)
        form.fields['nome'].widget.attrs = {'placeholder': 'Nome do Paciente',
                                            'maxlength': 50,
                                            'autocomplete': 'off'}
        form.fields['data_nascimento'].widget.attrs = {'placeholder': 'dd/mm/aaaa',
                                                       'maxlength': 10,
                                                       'autocomplete': 'off'}
        form.fields['responsavel'].widget.attrs = {'placeholder': 'Nome do Responsável pelo Paciente',
                                                   'maxlength': 50,
                                                   'autocomplete': 'off'}
        form.fields['cpf_responsavel'].widget.attrs = {'placeholder': '000.000.000-00',
                                                       'maxlength': 14,
                                                       'autocomplete': 'off'}
        return form


class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['nome', 'data_nascimento', 'responsavel', 'cpf_responsavel', 'ativo']
    template_name = 'paciente/edit.html'

    def get_context_data(self, **kwargs):
        context = super(PacienteUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = Paciente.objects.values_list('pk').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente editado
    def get_success_url(self):
        paciente_id = self.kwargs['pk']
        return reverse_lazy('details-paciente', kwargs={'pk': paciente_id})


class PacientesList(ListView):
    model = Paciente
    template_name = 'paciente/list.html'
    paginate_by = 12

    # buscar paciente por nome e se o mesmo está ativo
    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')
        if txt_nome:
            pacientes = Paciente.objects.filter(nome__icontains=txt_nome, ativo=True)
        else:
            pacientes = Paciente.objects.filter(ativo=True).order_by('nome', 'data_nascimento')
        return pacientes


class PacienteDetails(DetailView):
    queryset = Paciente.objects.all()
    template_name = 'paciente/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # recuperar os protocolos refente ao paciente

        context['primeira_unidade'] = PrimeiraUnidadeFuncional.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_avaliacao').select_related('paciente')
        context['segunda_unidade'] = SegundaUnidadeFuncional.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_avaliacao').select_related('paciente')
        context['terceira_unidade'] = TerceiraUnidadeFuncional.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_avaliacao').select_related('paciente')
        context['desenho_figura_humana'] = DesenhoFiguraHumana.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_avaliacao').select_related('paciente')
        context['anamnese_resultados'] = Anamnese.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_anamnese').select_related('paciente')
        context['conclusao'] = Conclusao.objects.filter(paciente=self.kwargs['pk']).order_by(
            'data_conclusao').select_related('paciente')

        # calcular a idade do paciente
        paciente_nascimento = Paciente.objects.values_list('data_nascimento').filter(pk=self.kwargs['pk'])

        data_nacimento = paciente_nascimento[0][0].toordinal()
        data_atual = datetime.date.today().toordinal()

        dias = data_atual - data_nacimento

        anos, dias = dias // 365, dias % 365
        meses, dias = dias // 30, dias % 30

        idade = None
        if anos <= 0 and meses < 0:
            idade = ''
        elif anos <= 0 and meses == 1:
            idade = f'{meses} mês'
        elif anos <= 0 and meses >= 2:
            idade = f'{meses} meses'
        elif anos == 1 and meses <= 0:
            idade = f'{anos} ano'
        elif anos >= 2 and meses <= 0:
            idade = f'{anos} anos'
        elif anos == 1 and meses == 1:
            idade = f'{anos} ano e {meses} mês'
        elif anos == 1 and meses >= 2:
            idade = f'{anos} ano e {meses} meses'
        elif anos >= 2 and meses == 1:
            idade = f'{anos} anos e {meses} mês'
        elif anos >= 2 and meses >= 2:
            idade = f'{anos} anos e {meses} meses'

        context['idade'] = idade

        return context


class PacientesInativosList(ListView):
    model = Paciente
    template_name = 'paciente/list-inativos.html'
    paginate_by = 12

    # buscar paciente por nome e se o mesmo está inativo
    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')
        if txt_nome:
            pacientes = Paciente.objects.filter(nome__icontains=txt_nome, ativo=False)
        else:
            pacientes = Paciente.objects.filter(ativo=False).order_by('nome', 'data_nascimento')
        return pacientes


# ------------------------- ANAMNESE -------------------------
class AnamneseCreate(CreateView):
    model = Anamnese
    fields = '__all__'
    template_name = 'anamnese/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(AnamneseCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)

        form.fields['motivos_da_consulta'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['idade_mae'].widget.attrs = {'autocomplete': 'off', 'min': 0}
        form.fields['idade_pai'].widget.attrs = {'autocomplete': 'off', 'min': 0}

        form.fields['intercorrencias_na_gestacao'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['medicacao_na_gestacao'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['traumas_fisicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['traumas_psiquicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['dependencia_quimica'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['peso'].widget.attrs = {'autocomplete': 'off', 'min': 0.0}
        form.fields['estatura'].widget.attrs = {'autocomplete': 'off', 'min': 0.0}
        form.fields['historico_primeiros_dias'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['doencas_familiares'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['doencas_e_acidentes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['disturbio_do_sono'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['rotina_do_sono'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['comportamento_social'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['tiques'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['sociabilidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['vida_cotidiana'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['eventos_da_vida'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['escolaridade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['rendimento_escolar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['queixa_escolar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['protidao_para_avd'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['ansiedades'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['inibicoes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['ensaios_terapeuticos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['conclusao_de_exames'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['aspectos_fisicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['saude_aparente'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['harmonia'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['desarmonia'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        return form


class AnamneseUpdate(UpdateView):
    model = Anamnese
    fields = '__all__'
    template_name = 'anamnese/edit.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(AnamneseUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)

        form.fields['motivos_da_consulta'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['idade_mae'].widget.attrs = {'autocomplete': 'off', 'min': 0}
        form.fields['idade_pai'].widget.attrs = {'autocomplete': 'off', 'min': 0}

        form.fields['intercorrencias_na_gestacao'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['medicacao_na_gestacao'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['traumas_fisicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['traumas_psiquicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['dependencia_quimica'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['peso'].widget.attrs = {'autocomplete': 'off'}
        form.fields['estatura'].widget.attrs = {'autocomplete': 'off'}
        form.fields['historico_primeiros_dias'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['doencas_familiares'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['doencas_e_acidentes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['disturbio_do_sono'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['rotina_do_sono'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['comportamento_social'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['tiques'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['sociabilidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['vida_cotidiana'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['eventos_da_vida'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['escolaridade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['rendimento_escolar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['queixa_escolar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['protidao_para_avd'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['ansiedades'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['inibicoes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        form.fields['ensaios_terapeuticos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['conclusao_de_exames'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['aspectos_fisicos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['saude_aparente'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['harmonia'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['desarmonia'].widget.attrs = {'autocomplete': 'off', 'rows': 3}

        return form

    def get_context_data(self, **kwargs):
        context = super(AnamneseUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = Anamnese.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente
    def get_success_url(self):
        anamnese = Anamnese.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        paciente = anamnese[0][0]
        return reverse_lazy('details-paciente', kwargs={'pk': paciente})


def render_pdf_anamnese(request, pk):
    template_path = 'anamnese/anamnese_pdf.html'

    # nome do paciente
    paciente_nome = Paciente.objects.values_list('nome').filter(pk=pk)

    # calcular a idade do paciente
    paciente_nascimento = Paciente.objects.values_list('data_nascimento').filter(pk=pk)
    data_nacimento = paciente_nascimento[0][0].toordinal()
    data_atual = datetime.date.today().toordinal()

    dias = data_atual - data_nacimento

    anos, dias = dias // 365, dias % 365
    meses, dias = dias // 30, dias % 30

    idade = None
    if anos <= 0 and meses < 0:
        idade = ''
    elif anos <= 0 and meses == 1:
        idade = f'{meses} mês'
    elif anos <= 0 and meses >= 2:
        idade = f'{meses} meses'
    elif anos == 1 and meses <= 0:
        idade = f'{anos} ano'
    elif anos >= 2 and meses <= 0:
        idade = f'{anos} anos'
    elif anos == 1 and meses == 1:
        idade = f'{anos} ano e {meses} mês'
    elif anos == 1 and meses >= 2:
        idade = f'{anos} ano e {meses} meses'
    elif anos >= 2 and meses == 1:
        idade = f'{anos} anos e {meses} mês'
    elif anos >= 2 and meses >= 2:
        idade = f'{anos} anos e {meses} meses'

    anamnese = Anamnese.objects.all().filter(paciente=pk)

    context = {
        # ---------------------------- Informações do Paciente ----------------------
        'nome': paciente_nome[0][0],
        'idade': idade,

        # ---------------------------- Anamnese ----------------------
        'anamnese_resultados': anamnese,
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # para download direto do pdf
    # response['Content-Disposition'] = 'attachment; filename="Relatorio {paciente_nome[0][0]} - {datetime.date.today().strftime("%d-%m-%Y")}.pdf"'
    # para visualizar o pdf
    response[
        'Content-Disposition'] = f'filename="Anamnese {paciente_nome[0][0]} - {datetime.date.today().strftime("%d-%m-%Y")}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('Errors <pre>' + html + '</pre>')
    return response


# ------------------------- PROTOCOLO -------------------------
class PrimeiraUnidadeFuncionalCreate(CreateView):
    model = PrimeiraUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/primeira_unidade/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(PrimeiraUnidadeFuncionalCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['obs_extensibilidade_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_extensibilidade_membros_inferiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_balanco_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tonico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tonico_cinetico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_imobilidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_equilibrio_estatico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form


class SegundaUnidadeFuncionalCreate(CreateView):
    model = SegundaUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/segunda_unidade/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(SegundaUnidadeFuncionalCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['nomeia_pontos_tateis'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 25}
        form.fields['imitacao_de_gestos'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 20}
        form.fields['obs_imitacao_de_gestos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_lateralizacoes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_reconhecimento_tatil'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['codificacao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['decodificacao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['transcodificacao_auditiva'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['transcodificacao_visual'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['obs_estruturacao_ritmica'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form


class TerceiraUnidadeFuncionalCreate(CreateView):
    model = TerceiraUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/terceira_unidade/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(TerceiraUnidadeFuncionalCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['obs_oculo_manual'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_oculo_pedal'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_dissociacao_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_dissociacao_membros_inferiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_pulseira_de_clipes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tamborilar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_grafomotricidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_quebra_cabeca'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['velocidade_precisao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 115}
        return form

class ConclusaoCreate(CreateView):
    model = Conclusao
    fields = '__all__'
    template_name = 'protocolo/conclusao/create.html'
    success_url = reverse_lazy('pacientes')
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(ConclusaoCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['psico_afetivo'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['psico_cognitivo'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['tonicidade'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['equilibracao'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['esquema_imagem_corporal'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['lateralizacao'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['estruturacao_espaco_temporal'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['praxia_global'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['praxia_fina'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['grafomotricidade'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['encaminhamento'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['prognostico'].widget.attrs = {'autocomplete': 'off', 'rows': 10}
        return form


class ConclusaoUpdate(UpdateView):
    model = Conclusao
    fields = '__all__'
    template_name = 'protocolo/conclusao/edit.html'
    success_url = reverse_lazy('pacientes')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(ConclusaoUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['psico_afetivo'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['psico_cognitivo'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['tonicidade'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['equilibracao'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['esquema_imagem_corporal'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['lateralizacao'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['estruturacao_espaco_temporal'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['praxia_global'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['praxia_fina'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['grafomotricidade'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['encaminhamento'].widget.attrs = {'autocomplete': 'off', 'rows': 6}
        form.fields['prognostico'].widget.attrs = {'autocomplete': 'off', 'rows': 10}
        return form


class DesenhoFiguraHumanaCreate(CreateView):
    model = DesenhoFiguraHumana
    fields = '__all__'
    template_name = 'protocolo/figura_humana/create.html'
    success_url = reverse_lazy('pacientes')

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(DesenhoFiguraHumanaCreate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['cabeca_presente']
        form.fields['pernas_presentes']
        form.fields['bracos_presentes']
        form.fields['tronco_presente']
        form.fields['comprimento_do_tronco_maior_que_largura']
        form.fields['ombros_definidamente_indicados']
        form.fields['bracos_pernas_ligados_ou_tronco']
        form.fields['bracos_pernas_ligados_ou_tronco_lugares_convenientes']
        form.fields['pescoco_presente']
        form.fields['contorno_do_pescoco_continuado']
        form.fields['olhos_presentes']
        form.fields['nariz_presente']
        form.fields['boca_presente']
        form.fields['nariz_boca_duas_dimensoes']
        form.fields['narinas']
        form.fields['cabelos']
        form.fields['cabelos_contorno_cabeca']
        form.fields['roupa']
        form.fields['duas_pecas_de_roupas']
        form.fields['desenho_sem_transparencia']
        form.fields['quatro_pecas_de_roupa']
        form.fields['traje_completo']
        form.fields['dedos_da_mao']
        form.fields['total_numero_de_dedos']
        form.fields['dedos_corretos']
        form.fields['oposicao_polegar']
        form.fields['maos_distinta_do_braco']
        form.fields['juntas_membros_sup']
        form.fields['juntas_membros_inf']
        form.fields['cabeca_tamanho_correto']
        form.fields['bracos_extensao_correta']
        form.fields['perna_extensao_correta']
        form.fields['pes_proporcionais']
        form.fields['bracos_e_pernas_proporcionais']
        form.fields['calcanhares']
        form.fields['linhas_firmes']
        form.fields['linhas_tracadas_e_firmes']
        form.fields['contorno_cabeca']
        form.fields['contorno_tronco']
        form.fields['contorno_bracos']
        form.fields['tracos_fisionomicos']
        form.fields['orelhas']
        form.fields['orelhas_proporcionais']
        form.fields['olhos_detalhados']
        form.fields['pupilas']
        form.fields['olhos_proporcionais']
        form.fields['olhar']
        form.fields['queixo_e_testa']
        form.fields['projecao_queixo']
        form.fields['corpo_em_perfil_transparencia']
        form.fields['corpo_em_perfil_sem_transparencia']

        form.fields['obs_desenho_figura_humana'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form


class PrimeiraUnidadeFuncionalUpdate(UpdateView):
    model = PrimeiraUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/primeira_unidade/edit.html'

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(PrimeiraUnidadeFuncionalUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['obs_extensibilidade_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_extensibilidade_membros_inferiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_balanco_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tonico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tonico_cinetico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_imobilidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_equilibrio_estatico'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form

    def get_context_data(self, **kwargs):
        context = super(PrimeiraUnidadeFuncionalUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = PrimeiraUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente editado
    def get_success_url(self):
        protocolo = PrimeiraUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        paciente = protocolo[0][0]
        return reverse_lazy('details-paciente', kwargs={'pk': paciente})


class SegundaUnidadeFuncionalUpdate(UpdateView):
    model = SegundaUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/segunda_unidade/edit.html'

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(SegundaUnidadeFuncionalUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['nomeia_pontos_tateis'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 25}
        form.fields['imitacao_de_gestos'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 20}
        form.fields['obs_imitacao_de_gestos'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_lateralizacoes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_reconhecimento_tatil'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['codificacao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['decodificacao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['transcodificacao_auditiva'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['transcodificacao_visual'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 21}
        form.fields['obs_estruturacao_ritmica'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form

    def get_context_data(self, **kwargs):
        context = super(SegundaUnidadeFuncionalUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = SegundaUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente editado
    def get_success_url(self):
        protocolo = SegundaUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        paciente = protocolo[0][0]
        return reverse_lazy('details-paciente', kwargs={'pk': paciente})


class TerceiraUnidadeFuncionalUpdate(UpdateView):
    model = TerceiraUnidadeFuncional
    fields = '__all__'
    template_name = 'protocolo/terceira_unidade/edit.html'

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(TerceiraUnidadeFuncionalUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['obs_oculo_manual'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_oculo_pedal'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_dissociacao_membros_superiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_dissociacao_membros_inferiores'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_pulseira_de_clipes'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_tamborilar'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_grafomotricidade'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['obs_quebra_cabeca'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        form.fields['velocidade_precisao'].widget.attrs = {'autocomplete': 'off', 'min': 0, 'max': 115}
        return form

    def get_context_data(self, **kwargs):
        context = super(TerceiraUnidadeFuncionalUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = TerceiraUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente editado
    def get_success_url(self):
        protocolo = TerceiraUnidadeFuncional.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        paciente = protocolo[0][0]
        return reverse_lazy('details-paciente', kwargs={'pk': paciente})


class DesenhoFiguraHumanaUpdate(UpdateView):
    model = DesenhoFiguraHumana
    fields = '__all__'
    template_name = 'protocolo/figura_humana/edit.html'

    # formatar inputs do formulario
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(DesenhoFiguraHumanaUpdate, self).get_form(form_class)
        form.fields['paciente'].queryset = Paciente.objects.filter(ativo=True)
        form.fields['cabeca_presente']
        form.fields['pernas_presentes']
        form.fields['bracos_presentes']
        form.fields['tronco_presente']
        form.fields['comprimento_do_tronco_maior_que_largura']
        form.fields['ombros_definidamente_indicados']
        form.fields['bracos_pernas_ligados_ou_tronco']
        form.fields['bracos_pernas_ligados_ou_tronco_lugares_convenientes']
        form.fields['pescoco_presente']
        form.fields['contorno_do_pescoco_continuado']
        form.fields['olhos_presentes']
        form.fields['nariz_presente']
        form.fields['boca_presente']
        form.fields['nariz_boca_duas_dimensoes']
        form.fields['narinas']
        form.fields['cabelos']
        form.fields['cabelos_contorno_cabeca']
        form.fields['roupa']
        form.fields['duas_pecas_de_roupas']
        form.fields['desenho_sem_transparencia']
        form.fields['quatro_pecas_de_roupa']
        form.fields['traje_completo']
        form.fields['dedos_da_mao']
        form.fields['total_numero_de_dedos']
        form.fields['dedos_corretos']
        form.fields['oposicao_polegar']
        form.fields['maos_distinta_do_braco']
        form.fields['juntas_membros_sup']
        form.fields['juntas_membros_inf']
        form.fields['cabeca_tamanho_correto']
        form.fields['bracos_extensao_correta']
        form.fields['perna_extensao_correta']
        form.fields['pes_proporcionais']
        form.fields['bracos_e_pernas_proporcionais']
        form.fields['calcanhares']
        form.fields['linhas_firmes']
        form.fields['linhas_tracadas_e_firmes']
        form.fields['contorno_cabeca']
        form.fields['contorno_tronco']
        form.fields['contorno_bracos']
        form.fields['tracos_fisionomicos']
        form.fields['orelhas']
        form.fields['orelhas_proporcionais']
        form.fields['olhos_detalhados']
        form.fields['pupilas']
        form.fields['olhos_proporcionais']
        form.fields['olhar']
        form.fields['queixo_e_testa']
        form.fields['projecao_queixo']
        form.fields['corpo_em_perfil_transparencia']
        form.fields['corpo_em_perfil_sem_transparencia']
        form.fields['obs_desenho_figura_humana'].widget.attrs = {'autocomplete': 'off', 'rows': 3}
        return form

    def get_context_data(self, **kwargs):
        context = super(DesenhoFiguraHumanaUpdate, self).get_context_data(**kwargs)

        # recuperar id do paciente, se o usuário optar por cancelar a edição, será redirecionado para a página de detalhes do paciente
        paciente = DesenhoFiguraHumana.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        context['id_paciente'] = paciente[0][0]
        return context

    # redirecionar para a pagina de detalhes do paciente editado
    def get_success_url(self):
        protocolo = DesenhoFiguraHumana.objects.values_list('paciente').filter(pk=self.kwargs['pk'])
        paciente = protocolo[0][0]
        return reverse_lazy('details-paciente', kwargs={'pk': paciente})


# ------------------------- RELATÓRIO -------------------------
class RelatorioView(TemplateView):
    template_name = 'relatorio/relatorio.html'

    def get_context_data(self, **kwargs):
        context = super(RelatorioView, self).get_context_data(**kwargs)

        # nome do paciente
        paciente_nome = Paciente.objects.values_list('nome').filter(pk=self.kwargs['pk'])

        # calcular a idade do paciente
        paciente_nascimento = Paciente.objects.values_list('data_nascimento').filter(pk=self.kwargs['pk'])
        data_nacimento = paciente_nascimento[0][0].toordinal()
        data_atual = datetime.date.today().toordinal()

        dias = data_atual - data_nacimento

        anos, dias = dias // 365, dias % 365
        meses, dias = dias // 30, dias % 30

        idade = None
        if anos <= 0 and meses < 0:
            idade = ''
        elif anos <= 0 and meses == 1:
            idade = f'{meses} mês'
        elif anos <= 0 and meses >= 2:
            idade = f'{meses} meses'
        elif anos == 1 and meses <= 0:
            idade = f'{anos} ano'
        elif anos >= 2 and meses <= 0:
            idade = f'{anos} anos'
        elif anos == 1 and meses == 1:
            idade = f'{anos} ano e {meses} mês'
        elif anos == 1 and meses >= 2:
            idade = f'{anos} ano e {meses} meses'
        elif anos >= 2 and meses == 1:
            idade = f'{anos} anos e {meses} mês'
        elif anos >= 2 and meses >= 2:
            idade = f'{anos} anos e {meses} meses'

        # id do paciente
        paciente = Paciente.objects.values_list('pk').filter(pk=self.kwargs['pk'])
        paciente_id = paciente[0][0]

        # dados sobre as unidades funcionais
        primeira_unidade = PrimeiraUnidadeFuncional.objects.all().filter(paciente=paciente_id).order_by(
            'data_avaliacao')
        segunda_unidade = SegundaUnidadeFuncional.objects.all().filter(paciente=paciente_id).order_by(
            'data_avaliacao')
        terceira_unidade = TerceiraUnidadeFuncional.objects.all().filter(paciente=paciente_id).order_by(
            'data_avaliacao')
        desenhos_figura_humana = DesenhoFiguraHumana.objects.all().filter(paciente=paciente_id).order_by(
            'data_avaliacao')

        # tabela goodenough
        df = unidades().topicos(paciente_id)[33]
        goodnough = tabela_goodnough(paciente_nascimento[0][0], df)

        # graficos referente ao protocolo
        graficos = executa_dataframes_e_graficos(paciente_id)

        # textos do relatório
        relatorio = relatorio_textos().df_unidade_relatorio(paciente_id)

        context = {
            # ---------------------------- Informações do Paciente ----------------------
            'nome': paciente_nome[0][0],
            'idade': idade,
            'id_paciente': paciente_id,

            # ---------------------------- Tabela Goodenough ----------------------
            'goodnough': goodnough,

            # ---------------------------- Dados do Protocolo -----------------------
            'primeira_unidade': primeira_unidade,
            'segunda_unidade': segunda_unidade,
            'terceira_unidade': terceira_unidade,
            'desenho_figura_humana': desenhos_figura_humana,

            # ---------------------------- Gráficos ----------------------
            # ---------------------------- Primeira Unidade Funcional ----------------------
            'conceitos_filogeneticos': graficos['conceitos_filogeneticos'],
            'extensibilidade': graficos['extensibilidade'],
            # 'balanco_passivo': graficos['balanco_passivo'],
            # 'paratonia': graficos['paratonia'],
            'diadococinesia': graficos['diadococinesia'],
            'sincinesia': graficos['sincinesia'],
            'imobilidade': graficos['imobilidade'],
            'equilibrio_estatico': graficos['equilibrio_estatico'],
            'equilibrio_dinamico_ponte': graficos['equilibrio_dinamico_ponte'],
            'equilibrio_dinamico_corda': graficos['equilibrio_dinamico_corda'],

            # ---------------------------- Segunda Unidade Funcional ----------------------
            'cinestesia': graficos['cinestesia'],
            'imitacao_de_gestos': graficos['imitacao_de_gestos'],
            #------USADO PARA GOOD---------
            'figura_humana': graficos['figura_humana'],
            'auto_imagem': graficos['auto_imagem'],
            # 'lateralizacoes': graficos['lateralizacoes'],
            # 'reconhecimento_direita_esquerda': graficos['reconhecimento_direita_esquerda'],
            'organizacao_perceptiva': graficos['organizacao_perceptiva'],
            'estruturacao_dinamica_espacial': graficos['estruturacao_dinamica_espacial'],
            'representacao_topografica': graficos['representacao_topografica'],
            'estruturacao_ritmica': graficos['estruturacao_ritmica'],

            # ---------------------------- Terceira Unidade Funcional ----------------------
            'oculo_manual': graficos['oculo_manual'],
            'oculo_pedal': graficos['oculo_pedal'],
            'dissociacao': graficos['dissociacao'],
            'agilidade': graficos['agilidade'],
            'pulseira_de_clipes': graficos['pulseira_de_clipes'],
            'tamborilar': graficos['tamborilar'],
            'velocidade_precisao': graficos['velocidade_precisao'],
            'tracados': graficos['tracados'],
            'pontilhados': graficos['pontilhados'],
            'circulos': graficos['circulos'],
            'cruz': graficos['cruz'],
            'colorir': graficos['colorir'],
            'quebra_cabeca': graficos['quebra_cabeca'],

            # ---------------------------- Relatório ----------------------
            # ---------------------------- Primeira Unidade Funcional ----------------------
            # ---------- conceitos filogeneticos ----------
            'txt_rolar': relatorio['rolar'][0],
            'json_rolar': relatorio['rolar'][1],
            'txt_engatinhar': relatorio['engatinhar'][0],
            'json_engatinhar': relatorio['engatinhar'][1],
            'txt_rastejar': relatorio['rastejar'][0],
            'json_rastejar': relatorio['rastejar'][1],
            # ---------- extensibilidade ----------
            'txt_extensibilidade_membros_superiores': relatorio['extensibilidade_membros_superiores'][0],
            'json_extensibilidade_membros_superiores': relatorio['extensibilidade_membros_superiores'][1],
            'txt_extensibilidade_membros_inferiores': relatorio['extensibilidade_membros_inferiores'][0],
            'json_extensibilidade_membros_inferiores': relatorio['extensibilidade_membros_inferiores'][1],
            # ---------- balanco passivo ----------
            'json_balanco_membros_superiores': relatorio['balanco_membros_superiores'][1],
            # ---------- paratonia ----------
            'json_paratonia_membros_superiores': relatorio['paratonia_membros_superiores'][1],
            # ---------- diadococinesia ----------
            'txt_pronacao': relatorio['pronacao'][0],
            'json_pronacao': relatorio['pronacao'][1],
            'txt_supinacao': relatorio['supinacao'][0],
            'json_supinacao': relatorio['supinacao'][1],
            # ---------- sincinesia ----------
            'txt_tonico': relatorio['tonico'][0],
            'json_tonico': relatorio['tonico'][1],
            'txt_tonico_cinetico': relatorio['tonico_cinetico'][0],
            'json_tonico_cinetico': relatorio['tonico_cinetico'][1],
            # ---------- imobilidade ----------
            'txt_imobilidade': relatorio['imobilidade'][0],
            'json_imobilidade': relatorio['imobilidade'][1],
            # ---------- equilibrio estatico ----------
            'txt_equilibrio_estatico': relatorio['equilibrio_estatico'][0],
            'json_equilibrio_estatico': relatorio['equilibrio_estatico'][1],
            # ---------- equilibrio dinamico ----------
            'txt_ponte_equilibrio_frente': relatorio['ponte_equilibrio_frente'][0],
            'json_ponte_equilibrio_frente': relatorio['ponte_equilibrio_frente'][1],
            'txt_ponte_equilibrio_tras': relatorio['ponte_equilibrio_tras'][0],
            'json_ponte_equilibrio_tras': relatorio['ponte_equilibrio_tras'][1],
            'txt_ponte_equilibrio_direita': relatorio['ponte_equilibrio_direita'][0],
            'json_ponte_equilibrio_direita': relatorio['ponte_equilibrio_direita'][1],
            'txt_ponte_equilibrio_esquerda': relatorio['ponte_equilibrio_esquerda'][0],
            'json_ponte_equilibrio_esquerda': relatorio['ponte_equilibrio_esquerda'][1],
            'txt_corda_olhos_abertos': relatorio['corda_olhos_abertos'][0],
            'json_corda_olhos_abertos': relatorio['corda_olhos_abertos'][1],
            'txt_corda_olhos_fechados': relatorio['corda_olhos_fechados'][0],
            'json_corda_olhos_fechados': relatorio['corda_olhos_fechados'][1],

            # ---------------------------- Segunda Unidade Funcional -----------------------
            # ---------- cinestesia ----------
            'txt_nomeia_pontos_tateis': relatorio['nomeia_pontos_tateis'][0],
            'json_nomeia_pontos_tateis': relatorio['nomeia_pontos_tateis'][1],
            # ---------- imitacao de gestos ----------
            'txt_imitacao_de_gestos': relatorio['imitacao_de_gestos'][0],
            'json_imitacao_de_gestos': relatorio['imitacao_de_gestos'][1],
            # ---------- auto-imagem ----------
            'txt_avaliador': relatorio['avaliador'][0],
            'json_avaliador': relatorio['avaliador'][1],
            'txt_em_si': relatorio['em_si'][0],
            'json_em_si': relatorio['em_si'][1],
            'txt_objeto': relatorio['objeto'][0],
            'json_objeto': relatorio['objeto'][1],
            # ---------- lateralizações ----------
            'json_lateralizacao_ocular': relatorio['lateralizacao_ocular'][1],
            'json_lateralizacao_manual': relatorio['lateralizacao_manual'][1],
            'json_lateralizacao_pedal': relatorio['lateralizacao_pedal'][1],
            # ---------- reconhecimento direita/esquerda ----------
            'txt_reconhecimento_verbal': relatorio['reconhecimento_verbal'][0],
            'json_reconhecimento_verbal': relatorio['reconhecimento_verbal'][1],
            'txt_reconhecimento_gestual': relatorio['reconhecimento_gestual'][0],
            'json_reconhecimento_gestual': relatorio['reconhecimento_gestual'][1],
            'txt_reconhecimento_tatil': relatorio['reconhecimento_tatil'][0],
            'json_reconhecimento_tatil': relatorio['reconhecimento_tatil'][1],
            # ---------- organização perceptiva ----------
            'txt_organizacao_perceptiva': relatorio['organizacao_perceptiva'][0],
            'json_organizacao_perceptiva': relatorio['organizacao_perceptiva'][1],
            # ---------- estruturação dinamica espacial ----------
            'txt_estruturacao_dinamica': relatorio['estruturacao_dinamica'][0],
            'json_estruturacao_dinamica': relatorio['estruturacao_dinamica'][1],
            # ---------- representação topografica ----------
            'txt_representacao_topografica': relatorio['representacao_topografica'][0],
            'json_representacao_topografica': relatorio['representacao_topografica'][1],
            # ---------- estruturação ritmica ----------
            'txt_codificacao': relatorio['codificacao'][0],
            'json_codificacao': relatorio['codificacao'][1],
            'txt_decodificacao': relatorio['decodificacao'][0],
            'json_decodificacao': relatorio['decodificacao'][1],
            'txt_transcodificacao_auditiva': relatorio['transcodificacao_auditiva'][0],
            'json_transcodificacao_auditiva': relatorio['transcodificacao_auditiva'][1],
            'txt_transcodificacao_visual': relatorio['transcodificacao_visual'][0],
            'json_transcodificacao_visual': relatorio['transcodificacao_visual'][1],

            # ---------------------------- Terceira Unidade Funcional -----------------------
            # ---------- coordenação oculo-manual ----------
            'txt_jogar_quatro_bolas': relatorio['jogar_quatro_bolas'][0],
            'json_jogar_quatro_bolas': relatorio['jogar_quatro_bolas'][1],
            'txt_agarrar_bola_de_tenis': relatorio['agarrar_bola_de_tenis'][0],
            'json_agarrar_bola_de_tenis': relatorio['agarrar_bola_de_tenis'][1],
            # ---------- coordenação oculo-pedal ----------
            'txt_quatro_chutes_ao_gol': relatorio['quatro_chutes_ao_gol'][0],
            'json_quatro_chutes_ao_gol': relatorio['quatro_chutes_ao_gol'][1],
            # ---------- dissociação ----------
            'txt_dissociacao_membros_superiores': relatorio['dissociacao_membros_superiores'][0],
            'json_dissociacao_membros_superiores': relatorio['dissociacao_membros_superiores'][1],
            'txt_dissociacao_membros_inferiores': relatorio['dissociacao_membros_inferiores'][0],
            'json_dissociacao_membros_inferiores': relatorio['dissociacao_membros_inferiores'][1],
            # ---------- agilidade ----------
            'txt_agilidade': relatorio['agilidade'][0],
            'json_agilidade': relatorio['agilidade'][1],
            # ---------- pulseira de clipes ----------
            'txt_pulseira_de_clipes': relatorio['pulseira_de_clipes'][0],
            'json_pulseira_de_clipes': relatorio['pulseira_de_clipes'][1],
            # ---------- tamborilar ----------
            'txt_tamborilar': relatorio['tamborilar'][0],
            'json_tamborilar': relatorio['tamborilar'][1],
            # ---------- velocidade e precisão ----------
            'txt_velocidade_precisao': relatorio['velocidade_precisao'][0],
            'json_velocidade_precisao': relatorio['velocidade_precisao'][1],
            # ---------- traçados ----------
            'txt_tracado_vertical': relatorio['tracado_vertical'][0],
            'json_tracado_vertical': relatorio['tracado_vertical'][1],
            'txt_tracado_horizontal': relatorio['tracado_horizontal'][0],
            'json_tracado_horizontal': relatorio['tracado_horizontal'][1],
            'txt_tracado_zig_zag': relatorio['tracado_zig_zag'][0],
            'json_tracado_zig_zag': relatorio['tracado_zig_zag'][1],
            'txt_tracado_curvo': relatorio['tracado_curvo'][0],
            'json_tracado_curvo': relatorio['tracado_curvo'][1],
            # ---------- pontilhados ----------
            'txt_pontilhados': relatorio['pontilhados'][0],
            'json_pontilhados': relatorio['pontilhados'][1],
            # ---------- circulos ----------
            'txt_circulos': relatorio['circulos'][0],
            'json_circulos': relatorio['circulos'][1],
            # ---------- cruz ----------
            'txt_cruz': relatorio['cruz'][0],
            'json_cruz': relatorio['cruz'][1],
            # ---------- colorir ----------
            'txt_colorir_graficamente': relatorio['colorir_graficamente'][1],
            'json_colorir_graficamente': relatorio['colorir_graficamente'][0],
        }
        return context


def render_pdf_view(request, pk):
    template_path = 'relatorio/relatorio_pdf.html'

    # nome do paciente
    paciente_nome = Paciente.objects.values_list('nome').filter(pk=pk)

    # calcular a idade do paciente
    paciente_nascimento = Paciente.objects.values_list('data_nascimento').filter(pk=pk)
    data_nacimento = paciente_nascimento[0][0].toordinal()
    data_atual = datetime.date.today().toordinal()

    dias = data_atual - data_nacimento

    anos, dias = dias // 365, dias % 365
    meses, dias = dias // 30, dias % 30

    idade = None
    if anos <= 0 and meses < 0:
        idade = ''
    elif anos <= 0 and meses == 1:
        idade = f'{meses} mês'
    elif anos <= 0 and meses >= 2:
        idade = f'{meses} meses'
    elif anos == 1 and meses <= 0:
        idade = f'{anos} ano'
    elif anos >= 2 and meses <= 0:
        idade = f'{anos} anos'
    elif anos == 1 and meses == 1:
        idade = f'{anos} ano e {meses} mês'
    elif anos == 1 and meses >= 2:
        idade = f'{anos} ano e {meses} meses'
    elif anos >= 2 and meses == 1:
        idade = f'{anos} anos e {meses} mês'
    elif anos >= 2 and meses >= 2:
        idade = f'{anos} anos e {meses} meses'

    # dados sobre as unidades funcionais
    primeira_unidade = PrimeiraUnidadeFuncional.objects.all().filter(paciente=pk).order_by(
        'data_avaliacao')
    segunda_unidade = SegundaUnidadeFuncional.objects.all().filter(paciente=pk).order_by(
        'data_avaliacao')
    terceira_unidade = TerceiraUnidadeFuncional.objects.all().filter(paciente=pk).order_by(
        'data_avaliacao')
    desenhos_figura_humana = DesenhoFiguraHumana.objects.all().filter(paciente=pk).order_by(
        'data_avaliacao')
    conclusao = Conclusao.objects.all().filter(paciente=pk).order_by(
        'data_conclusao')

    # textos do relatório
    relatorio = relatorio_textos().df_unidade_relatorio(pk)

    context = {
        # ---------------------------- Informações do Paciente ----------------------
        'nome': paciente_nome[0][0],
        'idade': idade,

        # ---------------------------- Datas -----------------------
        'primeira_unidade': primeira_unidade,
        'segunda_unidade': segunda_unidade,
        'terceira_unidade': terceira_unidade,
        'desenho_figura_humana': desenhos_figura_humana,
        'conclusao': conclusao,

        # ---------------------------- Relatório ----------------------
        # ---------------------------- Primeira Unidade Funcional ----------------------
        # ---------- conceitos filogeneticos ----------
        'txt_rolar': relatorio['rolar'][0],
        'json_rolar': relatorio['rolar'][1],
        'txt_engatinhar': relatorio['engatinhar'][0],
        'json_engatinhar': relatorio['engatinhar'][1],
        'txt_rastejar': relatorio['rastejar'][0],
        'json_rastejar': relatorio['rastejar'][1],
        # ---------- extensibilidade ----------
        'txt_extensibilidade_membros_superiores': relatorio['extensibilidade_membros_superiores'][0],
        'json_extensibilidade_membros_superiores': relatorio['extensibilidade_membros_superiores'][1],
        'txt_extensibilidade_membros_inferiores': relatorio['extensibilidade_membros_inferiores'][0],
        'json_extensibilidade_membros_inferiores': relatorio['extensibilidade_membros_inferiores'][1],
        # ---------- balanco passivo ----------
        'json_balanco_membros_superiores': relatorio['balanco_membros_superiores'][1],
        # ---------- paratonia ----------
        'json_paratonia_membros_superiores': relatorio['paratonia_membros_superiores'][1],
        # ---------- diadococinesia ----------
        'txt_pronacao': relatorio['pronacao'][0],
        'json_pronacao': relatorio['pronacao'][1],
        'txt_supinacao': relatorio['supinacao'][0],
        'json_supinacao': relatorio['supinacao'][1],
        # ---------- sincinesia ----------
        'txt_tonico': relatorio['tonico'][0],
        'json_tonico': relatorio['tonico'][1],
        'txt_tonico_cinetico': relatorio['tonico_cinetico'][0],
        'json_tonico_cinetico': relatorio['tonico_cinetico'][1],
        # ---------- imobilidade ----------
        'txt_imobilidade': relatorio['imobilidade'][0],
        'json_imobilidade': relatorio['imobilidade'][1],
        # ---------- equilibrio estatico ----------
        'txt_equilibrio_estatico': relatorio['equilibrio_estatico'][0],
        'json_equilibrio_estatico': relatorio['equilibrio_estatico'][1],
        # ---------- equilibrio dinamico ----------
        'txt_ponte_equilibrio_frente': relatorio['ponte_equilibrio_frente'][0],
        'json_ponte_equilibrio_frente': relatorio['ponte_equilibrio_frente'][1],
        'txt_ponte_equilibrio_tras': relatorio['ponte_equilibrio_tras'][0],
        'json_ponte_equilibrio_tras': relatorio['ponte_equilibrio_tras'][1],
        'txt_ponte_equilibrio_direita': relatorio['ponte_equilibrio_direita'][0],
        'json_ponte_equilibrio_direita': relatorio['ponte_equilibrio_direita'][1],
        'txt_ponte_equilibrio_esquerda': relatorio['ponte_equilibrio_esquerda'][0],
        'json_ponte_equilibrio_esquerda': relatorio['ponte_equilibrio_esquerda'][1],
        'txt_corda_olhos_abertos': relatorio['corda_olhos_abertos'][0],
        'json_corda_olhos_abertos': relatorio['corda_olhos_abertos'][1],
        'txt_corda_olhos_fechados': relatorio['corda_olhos_fechados'][0],
        'json_corda_olhos_fechados': relatorio['corda_olhos_fechados'][1],

        # ---------------------------- Segunda Unidade Funcional -----------------------
        # ---------- cinestesia ----------
        'txt_nomeia_pontos_tateis': relatorio['nomeia_pontos_tateis'][0],
        'json_nomeia_pontos_tateis': relatorio['nomeia_pontos_tateis'][1],
        # ---------- imitacao de gestos ----------
        'txt_imitacao_de_gestos': relatorio['imitacao_de_gestos'][0],
        'json_imitacao_de_gestos': relatorio['imitacao_de_gestos'][1],
        # ---------- auto-imagem ----------
        'txt_avaliador': relatorio['avaliador'][0],
        'json_avaliador': relatorio['avaliador'][1],
        'txt_em_si': relatorio['em_si'][0],
        'json_em_si': relatorio['em_si'][1],
        'txt_objeto': relatorio['objeto'][0],
        'json_objeto': relatorio['objeto'][1],
        # ---------- lateralizações ----------
        'json_lateralizacao_ocular': relatorio['lateralizacao_ocular'][1],
        'json_lateralizacao_manual': relatorio['lateralizacao_manual'][1],
        'json_lateralizacao_pedal': relatorio['lateralizacao_pedal'][1],
        # ---------- reconhecimento direita/esquerda ----------
        'txt_reconhecimento_verbal': relatorio['reconhecimento_verbal'][0],
        'json_reconhecimento_verbal': relatorio['reconhecimento_verbal'][1],
        'txt_reconhecimento_gestual': relatorio['reconhecimento_gestual'][0],
        'json_reconhecimento_gestual': relatorio['reconhecimento_gestual'][1],
        'txt_reconhecimento_tatil': relatorio['reconhecimento_tatil'][0],
        'json_reconhecimento_tatil': relatorio['reconhecimento_tatil'][1],
        # ---------- organização perceptiva ----------
        'txt_organizacao_perceptiva': relatorio['organizacao_perceptiva'][0],
        'json_organizacao_perceptiva': relatorio['organizacao_perceptiva'][1],
        # ---------- estruturação dinamica espacial ----------
        'txt_estruturacao_dinamica': relatorio['estruturacao_dinamica'][0],
        'json_estruturacao_dinamica': relatorio['estruturacao_dinamica'][1],
        # ---------- representação topografica ----------
        'txt_representacao_topografica': relatorio['representacao_topografica'][0],
        'json_representacao_topografica': relatorio['representacao_topografica'][1],
        # ---------- estruturação ritmica ----------
        'txt_codificacao': relatorio['codificacao'][0],
        'json_codificacao': relatorio['codificacao'][1],
        'txt_decodificacao': relatorio['decodificacao'][0],
        'json_decodificacao': relatorio['decodificacao'][1],
        'txt_transcodificacao_auditiva': relatorio['transcodificacao_auditiva'][0],
        'json_transcodificacao_auditiva': relatorio['transcodificacao_auditiva'][1],
        'txt_transcodificacao_visual': relatorio['transcodificacao_visual'][0],
        'json_transcodificacao_visual': relatorio['transcodificacao_visual'][1],

        # ---------------------------- Terceira Unidade Funcional -----------------------
        # ---------- coordenação oculo-manual ----------
        'txt_jogar_quatro_bolas': relatorio['jogar_quatro_bolas'][0],
        'json_jogar_quatro_bolas': relatorio['jogar_quatro_bolas'][1],
        'txt_agarrar_bola_de_tenis': relatorio['agarrar_bola_de_tenis'][0],
        'json_agarrar_bola_de_tenis': relatorio['agarrar_bola_de_tenis'][1],
        # ---------- coordenação oculo-pedal ----------
        'txt_quatro_chutes_ao_gol': relatorio['quatro_chutes_ao_gol'][0],
        'json_quatro_chutes_ao_gol': relatorio['quatro_chutes_ao_gol'][1],
        # ---------- dissociação ----------
        'txt_dissociacao_membros_superiores': relatorio['dissociacao_membros_superiores'][0],
        'json_dissociacao_membros_superiores': relatorio['dissociacao_membros_superiores'][1],
        'txt_dissociacao_membros_inferiores': relatorio['dissociacao_membros_inferiores'][0],
        'json_dissociacao_membros_inferiores': relatorio['dissociacao_membros_inferiores'][1],
        # ---------- agilidade ----------
        'txt_agilidade': relatorio['agilidade'][0],
        'json_agilidade': relatorio['agilidade'][1],
        # ---------- pulseira de clipes ----------
        'txt_pulseira_de_clipes': relatorio['pulseira_de_clipes'][0],
        'json_pulseira_de_clipes': relatorio['pulseira_de_clipes'][1],
        # ---------- tamborilar ----------
        'txt_tamborilar': relatorio['tamborilar'][0],
        'json_tamborilar': relatorio['tamborilar'][1],
        # ---------- velocidade e precisão ----------
        'txt_velocidade_precisao': relatorio['velocidade_precisao'][0],
        'json_velocidade_precisao': relatorio['velocidade_precisao'][1],
        # ---------- traçados ----------
        'txt_tracado_vertical': relatorio['tracado_vertical'][0],
        'json_tracado_vertical': relatorio['tracado_vertical'][1],
        'txt_tracado_horizontal': relatorio['tracado_horizontal'][0],
        'json_tracado_horizontal': relatorio['tracado_horizontal'][1],
        'txt_tracado_zig_zag': relatorio['tracado_zig_zag'][0],
        'json_tracado_zig_zag': relatorio['tracado_zig_zag'][1],
        'txt_tracado_curvo': relatorio['tracado_curvo'][0],
        'json_tracado_curvo': relatorio['tracado_curvo'][1],
        # ---------- pontilhados ----------
        'txt_pontilhados': relatorio['pontilhados'][0],
        'json_pontilhados': relatorio['pontilhados'][1],
        # ---------- circulos ----------
        'txt_circulos': relatorio['circulos'][0],
        'json_circulos': relatorio['circulos'][1],
        # ---------- cruz ----------
        'txt_cruz': relatorio['cruz'][0],
        'json_cruz': relatorio['cruz'][1],
        # ---------- colorir ----------
        'txt_colorir_graficamente': relatorio['colorir_graficamente'][1],
        'json_colorir_graficamente': relatorio['colorir_graficamente'][0],
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # para download direto do pdf
    # response['Content-Disposition'] = 'attachment; filename="Relatorio {paciente_nome[0][0]} - {datetime.date.today().strftime("%d-%m-%Y")}.pdf"'
    # para visualizar o pdf
    response[
        'Content-Disposition'] = f'filename="Relatorio {paciente_nome[0][0]} - {datetime.date.today().strftime("%d-%m-%Y")}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('Errors <pre>' + html + '</pre>')
    return response
