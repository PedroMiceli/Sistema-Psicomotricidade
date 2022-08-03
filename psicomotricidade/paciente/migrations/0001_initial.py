# Generated by Django 4.0.4 on 2022-07-18 16:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('responsavel', models.CharField(blank=True, max_length=50, null=True, verbose_name='Responsável')),
                ('cpf_responsavel', models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF do Responsável')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'pacientes',
                'ordering': ['nome', 'data_nascimento'],
            },
        ),
        migrations.CreateModel(
            name='TerceiraUnidadeFuncional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField(default=datetime.date(2022, 7, 18), verbose_name='Data de Avaliação')),
                ('jogar_quatro_bolas', models.CharField(blank=True, choices=[('Não realizou', 'Não realizou'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='Jogar 4 bolas ao cesto')),
                ('agarrar_bola_de_tenis', models.CharField(blank=True, choices=[('Não realizou', 'Não realizou'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='Agarrar a bola de tênis com as mãos')),
                ('obs_oculo_manual', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à coordenação óculo-manual')),
                ('quatro_chutes_ao_gol', models.CharField(blank=True, choices=[('0', 'Não acertou'), ('1', '1 chute'), ('2', '2 chutes'), ('3', '3 chutes'), ('4', '4 chutes')], max_length=1, null=True, verbose_name='4 chutes ao gol')),
                ('obs_oculo_pedal', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à coordenação óculo-pedal')),
                ('dissociacao_membros_superiores', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Membros superiores')),
                ('obs_dissociacao_membros_superiores', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos membros superiores')),
                ('dissociacao_membros_inferiores', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Membros inferiores')),
                ('obs_dissociacao_membros_inferiores', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos membros inferiores')),
                ('agilidade', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('pulseira_de_clipes', models.IntegerField(blank=True, help_text='Quantidade de clipes: 0 á 10', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('obs_pulseira_de_clipes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à pulseira de clipes')),
                ('tamborilar', models.CharField(blank=True, choices=[('Não realizou', 'Não realizou'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True)),
                ('obs_tamborilar', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à tamborilar')),
                ('velocidade_precisao', models.IntegerField(blank=True, help_text='Pontuação de 0 á 115', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(115)], verbose_name='Velocidade e precisão')),
                ('tracado_vertical', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Vertical')),
                ('tracado_horizontal', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Horizontal')),
                ('tracado_zig_zag', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Zig-zag')),
                ('tracado_curvo', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Curvos')),
                ('pontilhados', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('circulos', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Círculos')),
                ('cruz', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('colorir_graficamente', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Colorir graficamente em diferentes posições')),
                ('obs_grafomotricidade', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à grafomotricidade')),
                ('montar_quebra_cabeca', models.CharField(blank=True, choices=[('Não realizou', 'Não realizou'), ('4 peças', '4 peças'), ('8 peças', '8 peças'), ('10 peças', '10 peças')], max_length=12, null=True, verbose_name='Montar quebra-cabeça')),
                ('obs_quebra_cabeca', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à quebra-cabeça')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'terceira_unidade_funcional',
            },
        ),
        migrations.CreateModel(
            name='SegundaUnidadeFuncional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField(default=datetime.date(2022, 7, 18), verbose_name='Data de Avaliação')),
                ('nomeia_pontos_tateis', models.IntegerField(blank=True, help_text='Pontuação de 0 á 25', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)], verbose_name='Nomeia pontos táteis do corpo')),
                ('imitacao_de_gestos', models.IntegerField(blank=True, help_text='Pontuação de 0 á 20', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Imitação de gestos')),
                ('no_avaliador', models.CharField(blank=True, choices=[('Não possui repertório', 'Não possui repertório'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='No avaliador')),
                ('no_mesmo', models.CharField(blank=True, choices=[('Não possui repertório', 'Não possui repertório'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='No mesmo')),
                ('no_objeto', models.CharField(blank=True, choices=[('Não possui repertório', 'Não possui repertório'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='No objeto')),
                ('lateralizacao_ocular', models.CharField(blank=True, choices=[('Indefinida', 'Indefinida'), ('Esquerda', 'Esquerda'), ('Direita', 'Direita')], max_length=10, null=True, verbose_name='Lateralização ocular')),
                ('lateralizacao_manual', models.CharField(blank=True, choices=[('Indefinida', 'Indefinida'), ('Esquerda', 'Esquerda'), ('Direita', 'Direita')], max_length=10, null=True, verbose_name='Lateralização manual')),
                ('lateralizacao_pedal', models.CharField(blank=True, choices=[('Indefinida', 'Indefinida'), ('Esquerda', 'Esquerda'), ('Direita', 'Direita')], max_length=10, null=True, verbose_name='Lateralização pedal')),
                ('obs_lateralizacoes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente as lateralizações')),
                ('reconhecimento_verbal', models.CharField(blank=True, choices=[('Não reconheceu', 'Não reconheceu'), ('Reconhecimento parcial', 'Reconhecimento parcial'), ('Reconhecimento integral', 'Reconhecimento integral')], max_length=23, null=True, verbose_name='Verbal')),
                ('reconhecimento_gestual', models.CharField(blank=True, choices=[('Não reconheceu', 'Não reconheceu'), ('Reconhecimento parcial', 'Reconhecimento parcial'), ('Reconhecimento integral', 'Reconhecimento integral')], max_length=23, null=True, verbose_name='Gestual')),
                ('reconhecimento_tatil', models.CharField(blank=True, choices=[('Não reconheceu', 'Não reconheceu'), ('Reconhecimento parcial', 'Reconhecimento parcial'), ('Reconhecimento integral', 'Reconhecimento integral')], max_length=23, null=True, verbose_name='Tátil')),
                ('obs_reconhecimento_tatil', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente ao reconhecimento tátil')),
                ('organizacao_perceptiva', models.CharField(blank=True, choices=[('Não realizou', 'Não realizou'), ('Realizou parcialmente', 'Realizou parcialmente'), ('Realizou integralmente', 'Realizou integralmente')], max_length=22, null=True, verbose_name='Organização perceptiva')),
                ('estruturacao_dinamica_espacial', models.CharField(blank=True, choices=[('Não estruturou', 'Não estruturou'), ('Estruturou parcialmente', 'Estruturou parcialmente'), ('Estruturou integralmente', 'Estruturou integralmente')], max_length=24, null=True, verbose_name='Estruturação dinâmica espacial')),
                ('representacao_topografica', models.CharField(blank=True, choices=[('Não localizou-se', 'Não localizou-se'), ('Localizou-se parcialmente', 'Localizou-se parcialmente'), ('Localizou-se integralmente', 'Localizou-se integralmente')], max_length=26, null=True, verbose_name='Representação topográfica')),
                ('codificacao', models.IntegerField(blank=True, help_text='Pontuação de 0 á 21', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)], verbose_name='Codificação')),
                ('decodificacao', models.IntegerField(blank=True, help_text='Pontuação de 0 á 21', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)], verbose_name='Decodificação')),
                ('transcodificacao_auditiva', models.IntegerField(blank=True, help_text='Pontuação de 0 á 21', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)], verbose_name='Transcodificação auditiva')),
                ('transcodificacao_visual', models.IntegerField(blank=True, help_text='Pontuação de 0 á 21', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)], verbose_name='Transcodificação visual')),
                ('obs_estruturacao_ritmica', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente à estruturação rítmica')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'segunda_unidade_funcional',
            },
        ),
        migrations.CreateModel(
            name='PrimeiraUnidadeFuncional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField(default=datetime.date(2022, 7, 18), verbose_name='Data de Avaliação')),
                ('rolar', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('engatinhar', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('rastejar', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True)),
                ('extensibilidade_membros_superiores', models.CharField(blank=True, choices=[('Reduzida', 'Reduzida'), ('Aumentada', 'Aumentada'), ('Normal', 'Normal')], max_length=9, null=True, verbose_name='Membros superiores')),
                ('obs_extensibilidade_membros_superiores', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos membros superiores')),
                ('extensibilidade_membros_inferiores', models.CharField(blank=True, choices=[('Reduzida', 'Reduzida'), ('Aumentada', 'Aumentada'), ('Normal', 'Normal')], max_length=9, null=True, verbose_name='Membros inferiores')),
                ('obs_extensibilidade_membros_inferiores', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos membros inferiores')),
                ('balanco_membros_superiores', models.CharField(blank=True, choices=[('Movimentos pendulares', 'Movimentos pendulares'), ('Apresenta resistência', 'Apresenta resistência')], max_length=21, null=True, verbose_name='Membros superiores')),
                ('obs_balanco_membros_superiores', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos membros inferiores')),
                ('paratonia_membros_superiores', models.CharField(blank=True, choices=[('Sem paratonia', 'Sem paratonia'), ('Com paratonia', 'Com paratonia')], max_length=13, null=True, verbose_name='Membros superiores')),
                ('pronacao', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Pronação')),
                ('supinacao', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Supinação')),
                ('tonico', models.CharField(blank=True, choices=[('Nível alto', 'Nível alto'), ('Nível médio', 'Nível médio'), ('Nível baixo', 'Nível baixo'), ('Não apresenta', 'Não apresenta')], max_length=13, null=True, verbose_name='Tônico')),
                ('obs_tonico', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos movimentos tônicos')),
                ('tonico_cinetico', models.CharField(blank=True, choices=[('Nível alto', 'Nível alto'), ('Nível médio', 'Nível médio'), ('Nível baixo', 'Nível baixo'), ('Não apresenta', 'Não apresenta')], max_length=13, null=True, verbose_name='Tônico-cinético')),
                ('obs_tonico_cinetico', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações referente aos movimentos tônicos-cinéticos')),
                ('imobilidade', models.CharField(blank=True, choices=[('Sem imobilidade', 'Sem imobilidade'), ('Imobilidade parcial', 'Imobilidade parcial'), ('Imobilidade integral', 'Imobilidade integral')], max_length=20, null=True)),
                ('obs_imobilidade', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação referente à imobilidade')),
                ('equilibrio_estatico', models.CharField(blank=True, choices=[('Com dificuldade', 'Com dificuldade'), ('3 segundos', '3 segundos'), ('5 segundos', '5 segundos')], max_length=15, null=True, verbose_name='Equilíbrio estático')),
                ('obs_equilibrio_estatico', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação referente à equilíbrio estático')),
                ('ponte_equilibrio_frente', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Frente')),
                ('ponte_equilibrio_tras', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Trás')),
                ('ponte_equilibrio_direita', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Direita')),
                ('ponte_equilibrio_esquerda', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Esquerda')),
                ('corda_olhos_abertos', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Olhos abertos')),
                ('corda_olhos_fechados', models.CharField(blank=True, choices=[('1', 'Perfil 1'), ('2', 'Perfil 2'), ('3', 'Perfil 3'), ('4', 'Perfil 4')], max_length=1, null=True, verbose_name='Olhos fechados')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'primeira_unidade_funcional',
            },
        ),
        migrations.CreateModel(
            name='DesenhoFiguraHumana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateField(default=datetime.date(2022, 7, 18), verbose_name='Data de Avaliação')),
                ('desenho_figura_humana', models.IntegerField(blank=True, help_text='Pontuação de 0 á 43', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(43)], verbose_name='Desenho da figura humana')),
                ('obs_desenho_figura_humana', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação referente à desenho da figura humana')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'desenhos_figura_humana',
            },
        ),
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_anamnese', models.DateField(default=datetime.date(2022, 7, 18), verbose_name='Data de Anamnese')),
                ('nome_pai', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do pai')),
                ('nome_mae', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome da mãe')),
                ('irmaos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Irmãos (idades)')),
                ('motivos_da_consulta', models.TextField(blank=True, max_length=300, null=True)),
                ('idade_mae', models.IntegerField(blank=True, help_text='Em anos', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Idade da mãe na época da concepção')),
                ('profissao_mae', models.CharField(blank=True, max_length=150, null=True, verbose_name='Profissão da mãe na época da concepção')),
                ('idade_pai', models.IntegerField(blank=True, help_text='Em anos', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Idade do pai na época da concepção')),
                ('profissao_pai', models.CharField(blank=True, max_length=150, null=True, verbose_name='Profissão do pai na época da concepção')),
                ('planejamento_familiar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Houve planejamento familiar?')),
                ('intercorrencias_na_gestacao', models.TextField(blank=True, max_length=50, null=True, verbose_name='Intercorrências na gestação?')),
                ('medicacao_na_gestacao', models.TextField(blank=True, max_length=200, null=True, verbose_name='Fez uso de medicação na gravidez, qual?')),
                ('traumas_fisicos', models.TextField(blank=True, max_length=200, null=True, verbose_name='Traumas físicos?')),
                ('traumas_psiquicos', models.TextField(blank=True, max_length=200, null=True, verbose_name='Traumas psíquicos?')),
                ('dependencia_quimica', models.TextField(blank=True, max_length=200, null=True, verbose_name='Vícios ou dependência química?')),
                ('tipo_de_parto', models.CharField(blank=True, max_length=15, null=True)),
                ('duracao_parto', models.CharField(blank=True, max_length=10, null=True, verbose_name='Duração do parto')),
                ('posicao_nascimento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Posição de nascimento')),
                ('nota_apgar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nota APGAR')),
                ('peso', models.CharField(blank=True, help_text='Kg', max_length=5, null=True)),
                ('estatura', models.CharField(blank=True, help_text='Exemplo: 1,10', max_length=5, null=True)),
                ('chorou_ao_nascer', models.CharField(blank=True, max_length=20, null=True, verbose_name='Chorou ao nascer, choro forte ou fraco?')),
                ('aleitamento', models.CharField(blank=True, max_length=15, null=True, verbose_name='Aleitamento, até quando?')),
                ('historico_primeiros_dias', models.TextField(blank=True, max_length=500, null=True, verbose_name='Histórico dos primeiros dias de vida')),
                ('doencas_familiares', models.TextField(blank=True, max_length=300, null=True, verbose_name='Doenças familiares')),
                ('doencas_e_acidentes', models.TextField(blank=True, max_length=300, null=True, verbose_name='Doenças e acidentes graves')),
                ('disturbio_do_sono', models.TextField(blank=True, max_length=300, null=True, verbose_name='Teve algum distúrbio do sono?')),
                ('rotina_do_sono', models.TextField(blank=True, max_length=300, null=True, verbose_name='Qual a rotina do sono?')),
                ('fixou_a_cabeca', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fixou a cabeça com que idade?')),
                ('sorriu_com_que_idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Sorriu com que idade?')),
                ('sentou_com_que_idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Sentou com que idade?')),
                ('engatinhou', models.CharField(blank=True, max_length=20, null=True, verbose_name='Engatinhou?')),
                ('em_pe_com_apoio', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ficou em pé com apoio?')),
                ('andou_com_que_idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Andou com que idade?')),
                ('falou_com_que_idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Falou com?')),
                ('comportamento_social', models.TextField(blank=True, max_length=300, null=True)),
                ('tiques', models.TextField(blank=True, max_length=300, null=True)),
                ('sociabilidade', models.TextField(blank=True, max_length=300, null=True)),
                ('desfraldou_com_que_idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Desfraldou com?')),
                ('banheiro_com_independencia', models.CharField(blank=True, max_length=20, null=True, verbose_name='Usou o banheiro com independência com?')),
                ('enurese_noturna', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tem enurese noturna?')),
                ('vida_cotidiana', models.TextField(blank=True, max_length=500, null=True)),
                ('eventos_da_vida', models.TextField(blank=True, max_length=500, null=True, verbose_name='Principais eventos da vida da criança')),
                ('escolaridade', models.TextField(blank=True, max_length=100, null=True, verbose_name='A escolaridade')),
                ('rendimento_escolar', models.TextField(blank=True, max_length=300, null=True)),
                ('queixa_escolar', models.TextField(blank=True, max_length=300, null=True)),
                ('protidao_para_avd', models.TextField(blank=True, max_length=150, null=True, verbose_name='Tem prontidão para A.V.D.')),
                ('ansiedades', models.TextField(blank=True, max_length=300, null=True)),
                ('inibicoes', models.TextField(blank=True, max_length=300, null=True, verbose_name='Inibições')),
                ('ensaios_terapeuticos', models.TextField(blank=True, max_length=500, null=True, verbose_name='Ensaios terapêuticos já tentados')),
                ('conclusao_de_exames', models.TextField(blank=True, max_length=500, null=True, verbose_name='Conclusão de exames')),
                ('arquivos_conclusao_de_exames', models.FileField(blank=True, null=True, upload_to='arquivos/', verbose_name='Arquivo para conclusão de exames')),
                ('aspectos_fisicos', models.TextField(blank=True, max_length=500, null=True, verbose_name='Aspectos físicos e de desenvolvimento')),
                ('saude_aparente', models.TextField(blank=True, max_length=500, null=True, verbose_name='Saúde aparente')),
                ('harmonia', models.TextField(blank=True, max_length=500, null=True, verbose_name='Convive em harmonia')),
                ('desarmonia', models.TextField(blank=True, max_length=500, null=True, verbose_name='Convive em desarmonia')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'anamneses',
            },
        ),
    ]
