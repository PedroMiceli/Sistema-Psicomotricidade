import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# **** PACIENTE ****
class Paciente(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    responsavel = models.CharField(max_length=50, verbose_name='Responsável', null=True, blank=True)
    cpf_responsavel = models.CharField(max_length=14,
                                       verbose_name='Telefone do Responsável', null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} | {self.data_nascimento.strftime('%d/%m/%Y')}"

    class Meta:
        db_table = 'pacientes'
        ordering = ['nome', 'data_nascimento']


# **** ANAMNESE ****
class Anamnese(models.Model):
    paciente = models.ForeignKey(Paciente,unique=True, on_delete=models.PROTECT, verbose_name="Paciente")
    data_anamnese = models.DateField(verbose_name="Data de Anamnese", default=datetime.date.today())

    # Identificação
    nome_pai = models.CharField(max_length=50, verbose_name="Nome do pai", null=True, blank=True)
    nome_mae = models.CharField(max_length=50, verbose_name="Nome da mãe", null=True, blank=True)
    irmaos = models.CharField(max_length=200, verbose_name="Irmãos (idades)", null=True, blank=True)
    motivos_da_consulta = models.TextField(max_length=300, null=True, blank=True)

    # Dados da gestação
    idade_mae = models.IntegerField(validators=[MinValueValidator(0)],
                                    verbose_name="Idade da mãe na época da concepção",
                                    help_text="Em anos", null=True, blank=True)
    profissao_mae = models.CharField(max_length=150, verbose_name="Profissão da mãe na época da concepção", null=True,
                                     blank=True)
    idade_pai = models.IntegerField(validators=[MinValueValidator(0)],
                                    verbose_name="Idade do pai na época da concepção",
                                    help_text="Em anos", null=True, blank=True)
    profissao_pai = models.CharField(max_length=150, verbose_name="Profissão do pai na época da concepção", null=True,
                                     blank=True)
    planejamento_familiar = models.CharField(max_length=50, verbose_name="Houve planejamento familiar?", null=True,
                                             blank=True)
    intercorrencias_na_gestacao = models.TextField(max_length=50, verbose_name="Intercorrências na gestação?",
                                                   null=True, blank=True)
    medicacao_na_gestacao = models.TextField(max_length=200, verbose_name="Fez uso de medicação na gravidez, qual?",
                                             null=True, blank=True)
    traumas_fisicos = models.TextField(max_length=200, verbose_name="Traumas físicos?", null=True, blank=True)
    traumas_psiquicos = models.TextField(max_length=200, verbose_name="Traumas psíquicos?", null=True, blank=True)
    dependencia_quimica = models.TextField(max_length=200, verbose_name="Vícios ou dependência química?", null=True,
                                           blank=True)

    # Dados do parto
    tipo_de_parto = models.CharField(max_length=15, null=True, blank=True)
    duracao_parto = models.CharField(max_length=10, verbose_name="Duração do parto", null=True, blank=True)
    posicao_nascimento = models.CharField(max_length=50, verbose_name="Posição de nascimento", null=True, blank=True)
    nota_apgar = models.CharField(max_length=50, verbose_name="Nota APGAR", null=True, blank=True)
    peso = models.CharField(max_length=5, help_text="Kg", null=True, blank=True)
    estatura = models.CharField(max_length=5, help_text="Exemplo: 1,10", null=True, blank=True)
    chorou_ao_nascer = models.CharField(max_length=20, verbose_name="Chorou ao nascer, choro forte ou fraco?",
                                        null=True, blank=True)
    aleitamento = models.CharField(max_length=15, verbose_name="Aleitamento, até quando?", null=True, blank=True)
    historico_primeiros_dias = models.TextField(max_length=500, verbose_name="Histórico dos primeiros dias de vida",
                                                null=True, blank=True)

    # Antecedentes
    doencas_familiares = models.TextField(max_length=300, verbose_name="Doenças familiares", null=True, blank=True)
    doencas_e_acidentes = models.TextField(max_length=300, verbose_name="Doenças e acidentes graves", null=True,
                                           blank=True)

    disturbio_do_sono = models.TextField(max_length=300, verbose_name="Teve algum distúrbio do sono?", null=True,
                                         blank=True)
    rotina_do_sono = models.TextField(max_length=300, verbose_name="Qual a rotina do sono?", null=True, blank=True)

    fixou_a_cabeca = models.CharField(max_length=20, verbose_name="Fixou a cabeça com que idade?", null=True,
                                      blank=True)
    sorriu_com_que_idade = models.CharField(max_length=20, verbose_name="Sorriu com que idade?", null=True, blank=True)
    sentou_com_que_idade = models.CharField(max_length=20, verbose_name="Sentou com que idade?", null=True, blank=True)
    engatinhou = models.CharField(max_length=20, verbose_name="Engatinhou?", null=True, blank=True)
    em_pe_com_apoio = models.CharField(max_length=20, verbose_name="Ficou em pé com apoio?", null=True, blank=True)
    andou_com_que_idade = models.CharField(max_length=20, verbose_name="Andou com que idade?", null=True, blank=True)
    falou_com_que_idade = models.CharField(max_length=20, verbose_name="Falou com?", null=True, blank=True)

    comportamento_social = models.TextField(max_length=300, null=True, blank=True)
    tiques = models.TextField(max_length=300, null=True, blank=True)
    sociabilidade = models.TextField(max_length=300, null=True, blank=True)

    desfraldou_com_que_idade = models.CharField(max_length=20, verbose_name="Desfraldou com?", null=True, blank=True)
    banheiro_com_independencia = models.CharField(max_length=20, verbose_name="Usou o banheiro com independência com?",
                                                  null=True, blank=True)
    enurese_noturna = models.CharField(max_length=20, verbose_name="Tem enurese noturna?", null=True, blank=True)

    # Condições da vida diaria
    vida_cotidiana = models.TextField(max_length=500, null=True, blank=True)
    eventos_da_vida = models.TextField(max_length=500, verbose_name="Principais eventos da vida da criança", null=True,
                                       blank=True)
    escolaridade = models.TextField(max_length=100, verbose_name="A escolaridade", null=True, blank=True)
    rendimento_escolar = models.TextField(max_length=300, null=True, blank=True)
    queixa_escolar = models.TextField(max_length=300, null=True, blank=True)
    protidao_para_avd = models.TextField(max_length=150, verbose_name="Tem prontidão para A.V.D.", null=True,
                                         blank=True)

    # Adaptação a situações
    ansiedades = models.TextField(max_length=300, null=True, blank=True)
    inibicoes = models.TextField(max_length=300, verbose_name="Inibições", null=True, blank=True)

    # Antecedentes terapeuticos
    ensaios_terapeuticos = models.TextField(max_length=500, verbose_name="Ensaios terapêuticos já tentados", null=True,
                                            blank=True)
    conclusao_de_exames = models.TextField(max_length=500, verbose_name="Conclusão de exames", null=True, blank=True)
    arquivos_conclusao_de_exames = models.FileField(upload_to="arquivos/", null=True, blank=True,
                                                    verbose_name="Arquivo para conclusão de exames")
    aspectos_fisicos = models.TextField(max_length=500, verbose_name="Aspectos físicos e de desenvolvimento", null=True,
                                        blank=True)
    saude_aparente = models.TextField(max_length=500, verbose_name="Saúde aparente", null=True, blank=True)
    harmonia = models.TextField(max_length=500, verbose_name="Convive em harmonia", null=True, blank=True)
    desarmonia = models.TextField(max_length=500, verbose_name="Convive em desarmonia", null=True, blank=True)

    def __str__(self):
        return f"{self.paciente}"

    class Meta:
        db_table = 'anamneses'


# **** PROTOCOLO ****
OPTIONS_PERFIL_CHOICES = (
    ('1', 'Perfil 1'),
    ('2', 'Perfil 2'),
    ('3', 'Perfil 3'),
    ('4', 'Perfil 4')
)

# --------------------------- PRIMEIRA UNIDADE FUNCIONAL ---------------------------

OPTIONS_INTENSIDADE = (
    ('Reduzida', 'Reduzida'),
    ('Aumentada', 'Aumentada'),
    ('Normal', 'Normal'),
)

OPTIONS_BALANCO_PASSIVO = (
    ('Movimentos pendulares', 'Movimentos pendulares'),
    ('Apresenta resistência', 'Apresenta resistência')
)

OPTIONS_PARATONIA = (
    ('Sem paratonia', 'Sem paratonia'),
    ('Com paratonia', 'Com paratonia')
)

OPTIONS_SINCINESIA = (
    ('Nível alto', 'Nível alto'),
    ('Nível médio', 'Nível médio'),
    ('Nível baixo', 'Nível baixo'),
    ('Não apresenta', 'Não apresenta'),
)

OPTIONS_IMOBILIDADE = (
    ('Sem imobilidade', 'Sem imobilidade'),
    ('Imobilidade parcial', 'Imobilidade parcial'),
    ('Imobilidade integral', 'Imobilidade integral')
)

OPTIONS_EQUILIBRIO_ESTATICO = (
    ('Com dificuldade', 'Com dificuldade'),
    ('3 segundos', '3 segundos'),
    ('5 segundos', '5 segundos')
)

# --------------------------- SEGUNDA UNIDADE FUNCIONAL ---------------------------
OPTIONS_AUTO_IMAGEM = (
    ('Não possui repertório', 'Não possui repertório'),
    ('Realizou parcialmente', 'Realizou parcialmente'),
    ('Realizou integralmente', 'Realizou integralmente'),
)

OPTIONS_LATERALIZACAO = (
    ('Indefinida', 'Indefinida'),
    ('Esquerda', 'Esquerda'),
    ('Direita', 'Direita')
)

OPTIONS_RECONHECIMENTO = (
    ('Não reconheceu', 'Não reconheceu'),
    ('Reconhecimento parcial', 'Reconhecimento parcial'),
    ('Reconhecimento integral', 'Reconhecimento integral')
)

OPTIONS_ORGANIZACAO_PERCEPTIVA = (
    ('Não realizou', 'Não realizou'),
    ('Realizou parcialmente', 'Realizou parcialmente'),
    ('Realizou integralmente', 'Realizou integralmente'),
)

OPTIONS_ESTRUTURACAO_DINAMICA = (
    ('Não estruturou', 'Não estruturou'),
    ('Estruturou parcialmente', 'Estruturou parcialmente'),
    ('Estruturou integralmente', 'Estruturou integralmente'),
)

OPTIONS_REPRESENTACAO_TOPOGRAFICA = (
    ('Não localizou-se', 'Não localizou-se'),
    ('Localizou-se parcialmente', 'Localizou-se parcialmente'),
    ('Localizou-se integralmente', 'Localizou-se integralmente'),
)

# --------------------------- TERCEIRA UNIDADE FUNCIONAL ---------------------------
OPTIONS_OCULO_MANUAL = (
    ('Não realizou', 'Não realizou'),
    ('Realizou parcialmente', 'Realizou parcialmente'),
    ('Realizou integralmente', 'Realizou integralmente')
)

OPTIONS_OCULO_PEDAL = (
    ('0', 'Não acertou'),
    ('1', '1 chute'),
    ('2', '2 chutes'),
    ('3', '3 chutes'),
    ('4', '4 chutes'),
)

OPTIONS_TAMBORILAR = (
    ('Não realizou', 'Não realizou'),
    ('Realizou parcialmente', 'Realizou parcialmente'),
    ('Realizou integralmente', 'Realizou integralmente'),
)

OPTIONS_QUEBRA_CABECA = (
    ('Não realizou', 'Não realizou'),
    ('4 peças', '4 peças'),
    ('8 peças', '8 peças'),
    ('10 peças', '10 peças')
)


class PrimeiraUnidadeFuncional(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente")
    data_avaliacao = models.DateField(verbose_name="Data de Avaliação", default=datetime.date.today())

    # TONICIDADE
    # conceitos filogeneticos
    rolar = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)
    engatinhar = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)
    rastejar = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)

    # extensibilidade
    extensibilidade_membros_superiores = models.CharField(max_length=9, choices=OPTIONS_INTENSIDADE,
                                                          verbose_name="Membros superiores", null=True, blank=True)
    obs_extensibilidade_membros_superiores = models.TextField(max_length=1000, null=True, blank=True,
                                                              verbose_name="Observações referente aos membros superiores")
    extensibilidade_membros_inferiores = models.CharField(max_length=9, choices=OPTIONS_INTENSIDADE,
                                                          verbose_name="Membros inferiores", null=True, blank=True)
    obs_extensibilidade_membros_inferiores = models.TextField(max_length=1000, null=True, blank=True,
                                                              verbose_name="Observações referente aos membros inferiores")

    # balanço passivo
    balanco_membros_superiores = models.CharField(max_length=21, choices=OPTIONS_BALANCO_PASSIVO,
                                                  verbose_name="Membros superiores", null=True, blank=True)
    obs_balanco_membros_superiores = models.TextField(max_length=1000, null=True, blank=True,
                                                      verbose_name="Observações referente aos membros inferiores")
    # balanco_membros_inferiores = models.CharField(max_length=21, choices=OPTIONS_BALANCO_PASSIVO,
    #                                               verbose_name="Membros inferiores", null=True, blank=True)
    # obs_balanco_membros_inferiores = models.TextField(max_length=1000, null=True, blank=True,
    #                                                   verbose_name="Observações referente aos membros inferiores")

    # paratonia
    paratonia_membros_superiores = models.CharField(max_length=13, choices=OPTIONS_PARATONIA,
                                                    verbose_name="Membros superiores", null=True, blank=True)
    # paratonia_membros_inferiores = models.CharField(max_length=13, choices=OPTIONS_PARATONIA,
    #                                                 verbose_name="Membros inferiores", null=True, blank=True)

    # diadococinesia
    pronacao = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Pronação", null=True,
                                blank=True)
    supinacao = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Supinação", null=True,
                                 blank=True)

    # sincinesia
    tonico = models.CharField(max_length=13, choices=OPTIONS_SINCINESIA, verbose_name="Tônico", null=True, blank=True)
    obs_tonico = models.TextField(max_length=1000, null=True, blank=True,
                                  verbose_name="Observações referente aos movimentos tônicos")
    tonico_cinetico = models.CharField(max_length=13, choices=OPTIONS_SINCINESIA, verbose_name="Tônico-cinético",
                                       null=True, blank=True)
    obs_tonico_cinetico = models.TextField(max_length=1000, null=True, blank=True,
                                           verbose_name="Observações referente aos movimentos tônicos-cinéticos")

    # EQUILIBRAÇÃO
    # imobilidade
    imobilidade = models.CharField(max_length=20, choices=OPTIONS_IMOBILIDADE, null=True, blank=True)
    obs_imobilidade = models.TextField(max_length=1000, null=True, blank=True,
                                       verbose_name="Observação referente à imobilidade")

    # equilibrio estatico
    equilibrio_estatico = models.CharField(max_length=15, choices=OPTIONS_EQUILIBRIO_ESTATICO,
                                           verbose_name="Equilíbrio estático", null=True, blank=True)
    obs_equilibrio_estatico = models.TextField(max_length=1000, null=True, blank=True,
                                               verbose_name="Observação referente à equilíbrio estático")

    # equilibrio dinamico
    ponte_equilibrio_frente = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Frente",
                                               null=True, blank=True)
    ponte_equilibrio_tras = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Trás",
                                             null=True, blank=True)
    ponte_equilibrio_direita = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Direita",
                                                null=True, blank=True)
    ponte_equilibrio_esquerda = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Esquerda",
                                                 null=True, blank=True)

    corda_olhos_abertos = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Olhos abertos",
                                           null=True, blank=True)
    corda_olhos_fechados = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Olhos fechados",
                                            null=True, blank=True)

    def __str__(self):
        return f"{self.paciente} || {self.data_avaliacao}"

    class Meta:
        db_table = 'primeira_unidade_funcional'


class SegundaUnidadeFuncional(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente")
    data_avaliacao = models.DateField(verbose_name="Data de Avaliação", default=datetime.date.today())

    # NOÇÃO CORPORAL
    # cincinesia
    nomeia_pontos_tateis = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)],
                                               verbose_name="Nomeia pontos táteis do corpo",
                                               help_text="Pontuação de 0 á 25", null=True, blank=True)

    # imitação de gestos
    imitacao_de_gestos = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                                             verbose_name="Imitação de gestos", help_text="Pontuação de 0 á 20",
                                             null=True, blank=True)
    obs_imitacao_de_gestos = models.TextField(max_length=1000, null=True, blank=True,
                                                verbose_name="Observações referente à estruturação rítmica")

    # auto-imagem
    no_avaliador = models.CharField(max_length=22, choices=OPTIONS_AUTO_IMAGEM, null=True, blank=True,
                                    verbose_name="No avaliador")
    no_mesmo = models.CharField(max_length=22, choices=OPTIONS_AUTO_IMAGEM, null=True, blank=True,
                                verbose_name="No mesmo")
    no_objeto = models.CharField(max_length=22, choices=OPTIONS_AUTO_IMAGEM, null=True, blank=True,
                                 verbose_name="No objeto")

    # LATERALIZAÇÃO
    lateralizacao_ocular = models.CharField(max_length=10, choices=OPTIONS_LATERALIZACAO,
                                            verbose_name="Lateralização ocular", null=True, blank=True)
    lateralizacao_manual = models.CharField(max_length=10, choices=OPTIONS_LATERALIZACAO,
                                            verbose_name="Lateralização manual", null=True, blank=True)
    lateralizacao_pedal = models.CharField(max_length=10, choices=OPTIONS_LATERALIZACAO,
                                           verbose_name="Lateralização pedal", null=True, blank=True)
    obs_lateralizacoes = models.TextField(max_length=1000, null=True, blank=True,
                                          verbose_name="Observações referente as lateralizações")

    # reconhecimento direita/esquerda
    reconhecimento_verbal = models.CharField(max_length=23, choices=OPTIONS_RECONHECIMENTO, verbose_name="Verbal",
                                             null=True, blank=True)
    reconhecimento_gestual = models.CharField(max_length=23, choices=OPTIONS_RECONHECIMENTO, verbose_name="Gestual",
                                              null=True, blank=True)
    reconhecimento_tatil = models.CharField(max_length=23, choices=OPTIONS_RECONHECIMENTO, verbose_name="Tátil",
                                            null=True, blank=True)
    obs_reconhecimento_tatil = models.TextField(max_length=1000, null=True, blank=True,
                                                verbose_name="Observações referente ao reconhecimento tátil")

    # ESTRUTURAÇÃO ESPAÇO TEMPORAL
    organizacao_perceptiva = models.CharField(max_length=22, choices=OPTIONS_ORGANIZACAO_PERCEPTIVA,
                                              verbose_name="Organização perceptiva", null=True, blank=True)
    estruturacao_dinamica_espacial = models.CharField(max_length=24, choices=OPTIONS_ESTRUTURACAO_DINAMICA,
                                                      verbose_name="Estruturação dinâmica espacial", null=True,
                                                      blank=True)
    representacao_topografica = models.CharField(max_length=26, choices=OPTIONS_REPRESENTACAO_TOPOGRAFICA,
                                                 verbose_name="Representação topográfica", null=True, blank=True)

    # estruturação ritmica
    codificacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21)], null=True, blank=True,
                                      verbose_name="Codificação", help_text="Pontuação de 0 á 21")
    decodificacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21)], null=True, blank=True,
                                        verbose_name="Decodificação", help_text="Pontuação de 0 á 21")
    transcodificacao_auditiva = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21)], null=True,
                                                    blank=True, verbose_name="Transcodificação auditiva",
                                                    help_text="Pontuação de 0 á 21")
    transcodificacao_visual = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(21)], null=True,
                                                  blank=True, verbose_name="Transcodificação visual",
                                                  help_text="Pontuação de 0 á 21")
    obs_estruturacao_ritmica = models.TextField(max_length=1000, null=True, blank=True,
                                                verbose_name="Observações referente à estruturação rítmica")

    def __str__(self):
        return f"{self.paciente} || {self.data_avaliacao}"

    class Meta:
        db_table = 'segunda_unidade_funcional'


class TerceiraUnidadeFuncional(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente")
    data_avaliacao = models.DateField(verbose_name="Data de Avaliação", default=datetime.date.today())

    # PRAXIA GLOBAL
    # coordenação oculo-manual
    jogar_quatro_bolas = models.CharField(max_length=22, choices=OPTIONS_OCULO_MANUAL,
                                          verbose_name="Jogar 4 bolas ao cesto", null=True, blank=True)
    agarrar_bola_de_tenis = models.CharField(max_length=22, choices=OPTIONS_OCULO_MANUAL,
                                             verbose_name="Agarrar a bola de tênis com as mãos", null=True, blank=True)
    obs_oculo_manual = models.TextField(max_length=1000, null=True, blank=True,
                                        verbose_name="Observações referente à coordenação óculo-manual")

    # coordenação oculo-pedal
    quatro_chutes_ao_gol = models.CharField(max_length=1, choices=OPTIONS_OCULO_PEDAL, verbose_name="4 chutes ao gol",
                                            null=True, blank=True)
    obs_oculo_pedal = models.TextField(max_length=1000, null=True, blank=True,
                                       verbose_name="Observações referente à coordenação óculo-pedal")

    # dissociação
    dissociacao_membros_superiores = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES,
                                                      verbose_name="Membros superiores", null=True, blank=True)
    obs_dissociacao_membros_superiores = models.TextField(max_length=1000, null=True, blank=True,
                                                          verbose_name="Observações referente aos membros superiores")
    dissociacao_membros_inferiores = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES,
                                                      verbose_name="Membros inferiores", null=True, blank=True)
    obs_dissociacao_membros_inferiores = models.TextField(max_length=1000, null=True, blank=True,
                                                          verbose_name="Observações referente aos membros inferiores")

    # agilidade
    agilidade = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)

    # PRAXIA FINA
    pulseira_de_clipes = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                             help_text="Quantidade de clipes: 0 á 10", null=True, blank=True)
    obs_pulseira_de_clipes = models.TextField(max_length=1000, null=True, blank=True,
                                              verbose_name="Observações referente à pulseira de clipes")
    tamborilar = models.CharField(max_length=22, choices=OPTIONS_TAMBORILAR, null=True, blank=True)
    obs_tamborilar = models.TextField(max_length=1000, null=True, blank=True,
                                      verbose_name="Observações referente à tamborilar")
    velocidade_precisao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(115)],
                                              verbose_name="Velocidade e precisão", help_text="Pontuação de 0 á 115",
                                              null=True, blank=True)

    # GRAFOMOTRICIDADE
    tracado_vertical = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Vertical",
                                        null=True, blank=True)
    tracado_horizontal = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Horizontal",
                                          null=True, blank=True)
    tracado_zig_zag = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Zig-zag", null=True,
                                       blank=True)
    tracado_curvo = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Curvos", null=True,
                                     blank=True)

    pontilhados = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)
    circulos = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, verbose_name="Círculos", null=True, blank=True)
    cruz = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES, null=True, blank=True)
    colorir_graficamente = models.CharField(max_length=1, choices=OPTIONS_PERFIL_CHOICES,
                                            verbose_name="Colorir graficamente em diferentes posições", null=True, blank=True)
    obs_grafomotricidade = models.TextField(max_length=1000, null=True, blank=True,
                                            verbose_name="Observações referente à grafomotricidade")

    # MONTAR QUEBRA-CABEÇA
    montar_quebra_cabeca = models.CharField(max_length=12, choices=OPTIONS_QUEBRA_CABECA,
                                            verbose_name="Montar quebra-cabeça", null=True, blank=True)
    obs_quebra_cabeca = models.TextField(max_length=1000, null=True, blank=True,
                                         verbose_name="Observações referente à quebra-cabeça")

    def __str__(self):
        return f"{self.paciente} || {self.data_avaliacao}"

    class Meta:
        db_table = 'terceira_unidade_funcional'


class DesenhoFiguraHumana(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente")
    data_avaliacao = models.DateField(verbose_name="Data de Avaliação", default=datetime.date.today())

    # desenho da figura humana
    #desenho_figura_humana = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(51)],verbose_name="Desenho da figura humana",help_text="Pontuação de 0 á 51", null=True, blank=True)

    cabeca_presente = models.BooleanField(default=False, verbose_name="Se a cabeça está presente.")
    pernas_presentes = models.BooleanField(default=False, verbose_name="Se as pernas estão presentes.")
    bracos_presentes = models.BooleanField(default=False, verbose_name="Se os braços estão presentes.")
    tronco_presente = models.BooleanField(default=False, verbose_name="Se o tronco está presente.")
    comprimento_do_tronco_maior_que_largura = models.BooleanField(default=False, verbose_name="Comprimento do tronco maior que a largura.")
    ombros_definidamente_indicados = models.BooleanField(default=False, verbose_name="Ombros definidamente indicados.")
    bracos_pernas_ligados_ou_tronco = models.BooleanField(default=False, verbose_name="Braços e pernas ligados ao tronco, seja qual for o ponto de ligação")
    bracos_pernas_ligados_ou_tronco_lugares_convenientes = models.BooleanField(default=False, verbose_name="Braços e pernas ligados ao tronco nos lugares convenientes.")
    pescoco_presente = models.BooleanField(default=False, verbose_name="Se o pescoço está presente.")
    contorno_do_pescoco_continuado = models.BooleanField(default=False, verbose_name="Contorno do pescoço continuado da cabeça ou do tronco, ou o de ambos.")
    olhos_presentes = models.BooleanField(default=False, verbose_name="Se os olhos estão presentes.")
    nariz_presente = models.BooleanField(default=False, verbose_name="Se o nariz esta presente.")
    boca_presente = models.BooleanField(default=False, verbose_name="Se a boca está presente.")
    nariz_boca_duas_dimensoes = models.BooleanField(default=False, verbose_name="Nariz e boca representados em duas dimensões, os dois lábios indicados.")
    narinas = models.BooleanField(default=False, verbose_name="Se as narinas estão representadas.")
    cabelos = models.BooleanField(default=False, verbose_name="Se os cabelos estão representados.")
    cabelos_contorno_cabeca = models.BooleanField(default=False, verbose_name="Cabelos desenhados sem acompanharem o contorno da cabeça a qual deve transparecer entre os cabelos.")
    roupa = models.BooleanField(default=False, verbose_name="Se as roupas esta representada.")
    duas_pecas_de_roupas = models.BooleanField(default=False, verbose_name="Duas peças de roupa pelo menos representadas sem deixar transparecer partes que cobrem.")
    desenho_sem_transparencia = models.BooleanField(default=False, verbose_name="Desenho sem nenhuma transparencia, além disso, representação das mangas e das calças.")
    quatro_pecas_de_roupa = models.BooleanField(default=False, verbose_name="Quatro peças de roupa pelo menos, representadas de modo inequívoco.")
    traje_completo = models.BooleanField(default=False, verbose_name="Traje comleto sem incongruência.")
    dedos_da_mao = models.BooleanField(default=False, verbose_name="Se os dedos da mão estão representados.")
    total_numero_de_dedos = models.BooleanField(default=False, verbose_name="Se o exato numero de dedos está representado.")
    dedos_corretos = models.BooleanField(default=False, verbose_name="Dedos representados em duas dimensões, o comprimento maior que a largura e o ângulo entre os dedos não maior que 180º graus.")
    oposicao_polegar = models.BooleanField(default=False, verbose_name="Oposição do polegar, palma da mão representada.")
    maos_distinta_do_braco = models.BooleanField(default=False, verbose_name="Mão representada como parte distinta do braço e dos dedos.")
    juntas_membros_sup = models.BooleanField(default=False, verbose_name="Representação de uma das juntas dos membros superiores.")
    juntas_membros_inf = models.BooleanField(default=False, verbose_name="Representação de uma das juntas dos membros inferiores.")
    cabeca_tamanho_correto = models.BooleanField(default=False, verbose_name="Tamanho da cabeça não maior que a metade, nem menor que um décimo do corpo.")
    bracos_extensao_correta = models.BooleanField(default=False, verbose_name="Braços de extensão igual ao comprimento do tronco, ou puco maior que ele.")
    perna_extensao_correta = models.BooleanField(default=False, verbose_name="Extensão das pernas não menor, nem duas vezes maior que o tronco.")
    pes_proporcionais = models.BooleanField(default=False, verbose_name="Pés proporcionais em relação ao corpo.")
    bracos_e_pernas_proporcionais = models.BooleanField(default=False, verbose_name="Braços e pernas proporcionais e representados em duas dimensões.")
    calcanhares = models.BooleanField(default=False, verbose_name="Se os calcanhares estão representados.")
    linhas_firmes = models.BooleanField(default=False, verbose_name="Todas as linhas firmes, encontrando-se sem se ultrapassarem mutuamente ou sem deixarem espaços.")
    linhas_tracadas_e_firmes = models.BooleanField(default=False, verbose_name="Todas as linhas além de traçadas com firmeza,com seus pontos de união inteiramente exatos.")
    contorno_cabeca = models.BooleanField(default=False, verbose_name="Contorno da cabeça, sem nehnuma irregularidade.")
    contorno_tronco = models.BooleanField(default=False, verbose_name="Contorno do tronco, sem nenhuma irregularidade.")
    contorno_bracos = models.BooleanField(default=False, verbose_name="Contorno dos braços e pernas sem nenhuma irregularidade.")
    tracos_fisionomicos = models.BooleanField(default=False, verbose_name="Traços fisionõmicos sem nenhuma irregularidade.")
    orelhas = models.BooleanField(default=False, verbose_name="Representação das orelhas.")
    orelhas_proporcionais = models.BooleanField(default=False, verbose_name="Orelhas proporcionais e colocadas em posições exatas.")
    olhos_detalhados = models.BooleanField(default=False, verbose_name="Representação das particularidades relativas dos olhos.")
    pupilas = models.BooleanField(default=False, verbose_name="Representação das pupilas.")
    olhos_proporcionais = models.BooleanField(default=False, verbose_name="Olhos proporcionais.")
    olhar = models.BooleanField(default=False, verbose_name="Representação correta do olhar.")
    queixo_e_testa = models.BooleanField(default=False, verbose_name="Representação do queixo e da testa.")
    projecao_queixo = models.BooleanField(default=False, verbose_name="Projeção do queixo representada.")
    corpo_em_perfil_transparencia = models.BooleanField(default=False, verbose_name="Representação de todo o corpo em perfil, embora com transparência.")
    corpo_em_perfil_sem_transparencia = models.BooleanField(default=False, verbose_name="Representação de todo o corpo em perfil sem nenhum erro e sem transparência.")

    obs_desenho_figura_humana = models.TextField(max_length=1000, null=True, blank=True,
                                                 verbose_name="Observação referente à desenho da figura humana")

    def __str__(self):
        return f"{self.paciente} || {self.data_avaliacao}"

    class Meta:
        db_table = 'desenhos_figura_humana'


class Conclusao(models.Model):
    paciente = models.ForeignKey(Paciente,unique=True, on_delete=models.PROTECT, verbose_name="Paciente")
    data_conclusao = models.DateField(verbose_name="Data da Conclusão", default=datetime.date.today())
    # -------------------- Aspectos psico cognitivos e afetivos ----------
    psico_afetivo = models.TextField(max_length=500, verbose_name="Aspectos Psico-Afetivos", null=True, blank=True)
    psico_cognitivo = models.TextField(max_length=500, verbose_name="Aspectos Psico-Cognitivos", null=True, blank=True)
    # ------------------- parecer --------------
    tonicidade = models.TextField(max_length=500, verbose_name="Tonicidade", null=True, blank=True)
    equilibracao = models.TextField(max_length=500, verbose_name="Equilibração", null=True, blank=True)
    esquema_imagem_corporal = models.TextField(max_length=500, verbose_name="Esquema e Imagem Corporal", null=True, blank=True)
    lateralizacao = models.TextField(max_length=500, verbose_name="Lateralização", null=True, blank=True)
    estruturacao_espaco_temporal = models.TextField(max_length=500, verbose_name="Estruturação Espaço-Temporal", null=True, blank=True)
    praxia_global = models.TextField(max_length=500, verbose_name="Praxia Global", null=True, blank=True)
    praxia_fina = models.TextField(max_length=500, verbose_name="Praxia Fina", null=True, blank=True)
    grafomotricidade = models.TextField(max_length=500, verbose_name="Grafomotricidade", null=True, blank=True)
    # -------------------- Encaminhamento -------------------
    encaminhamento = models.TextField(max_length=500, verbose_name="Encaminhamento", null=True, blank=True)
    # ------------------- prognostico ---------------------
    prognostico = models.TextField(max_length=1000, verbose_name="Prognóstico", null=True, blank=True)

    def __str__(self):
        return f"{self.paciente} || {self.data_avaliacao}"

    class Meta:
        db_table = 'conclusao'
