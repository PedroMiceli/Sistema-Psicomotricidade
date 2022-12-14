# Generated by Django 4.0.4 on 2022-08-04 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_alter_anamnese_data_anamnese_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desenhofigurahumana',
            name='desenho_figura_humana',
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='boca_presente',
            field=models.BooleanField(default=False, verbose_name='Se a boca está presente.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='bracos_e_pernas_proporcionais',
            field=models.BooleanField(default=False, verbose_name='Braços e pernas proporcionais e representados em duas dimensões.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='bracos_extensao_correta',
            field=models.BooleanField(default=False, verbose_name='Braços de extensão igual ao comprimento do tronco, ou puco maior que ele.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='bracos_pernas_ligados_ou_tronco',
            field=models.BooleanField(default=False, verbose_name='Braços e pernas ligados ao tronco, seja qual for o ponto de ligação'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='bracos_pernas_ligados_ou_tronco_lugares_convenientes',
            field=models.BooleanField(default=False, verbose_name='Braços e pernas ligados ao tronco nos lugares convenientes.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='bracos_presentes',
            field=models.BooleanField(default=False, verbose_name='Se os braços estão presentes.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='cabeca_presente',
            field=models.BooleanField(default=False, verbose_name='Se a cabeça está presente.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='cabeca_tamanho_correto',
            field=models.BooleanField(default=False, verbose_name='Tamanho da cabeça não maior que a metade, nem menor que um décimo do corpo.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='cabelos',
            field=models.BooleanField(default=False, verbose_name='Se os cabelos estão representados.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='cabelos_contorno_cabeca',
            field=models.BooleanField(default=False, verbose_name='Cabelos desenhados sem acompanharem o contorno da cabeça a qual deve transparecer entre os cabelos.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='calcanhares',
            field=models.BooleanField(default=False, verbose_name='Se os calcanhares estão representados.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='comprimento_do_tronco_maior_que_largura',
            field=models.BooleanField(default=False, verbose_name='Comprimento do tronco maior que a largura.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='contorno_bracos',
            field=models.BooleanField(default=False, verbose_name='Contorno dos braços e pernas sem nenhuma irregularidade.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='contorno_cabeca',
            field=models.BooleanField(default=False, verbose_name='Contorno da cabeça, sem nehnuma irregularidade.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='contorno_do_pescoco_continuado',
            field=models.BooleanField(default=False, verbose_name='Contorno do pescoço continuado da cabeça ou do tronco, ou o de ambos.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='contorno_tronco',
            field=models.BooleanField(default=False, verbose_name='Contorno do tronco, sem nenhuma irregularidade.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='corpo_em_perfil_sem_transparencia',
            field=models.BooleanField(default=False, verbose_name='Representação de todo o corpo em perfil sem nenhum erro e sem transparência.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='corpo_em_perfil_transparencia',
            field=models.BooleanField(default=False, verbose_name='Representação de todo o corpo em perfil, embora com transparência.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='dedos_corretos',
            field=models.BooleanField(default=False, verbose_name='Dedos representados em duas dimensões, o comprimento maior que a largura e o ângulo entre os dedos não maior que 180º graus.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='dedos_da_mao',
            field=models.BooleanField(default=False, verbose_name='Se os dedos da mão estão representados.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='desenho_sem_transparencia',
            field=models.BooleanField(default=False, verbose_name='Desenho sem nenhuma transparencia, além disso, representação das mangas e das calças.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='duas_pecas_de_roupas',
            field=models.BooleanField(default=False, verbose_name='Duas peças de roupa pelo menos representadas sem deixar transparecer partes que cobrem.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='juntas_membros_inf',
            field=models.BooleanField(default=False, verbose_name='Representação de uma das juntas dos membros inferiores.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='juntas_membros_sup',
            field=models.BooleanField(default=False, verbose_name='Representação de uma das juntas dos membros superiores.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='linhas_firmes',
            field=models.BooleanField(default=False, verbose_name='Todas as linhas firmes, encontrando-se sem se ultrapassarem mutuamente ou sem deixarem espaços.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='linhas_tracadas_e_firmes',
            field=models.BooleanField(default=False, verbose_name='Todas as linhas além de traçadas com firmeza,com seus pontos de união inteiramente exatos.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='maos_distinta_do_braco',
            field=models.BooleanField(default=False, verbose_name='Mão representada como parte distinta do braço e dos dedos.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='narinas',
            field=models.BooleanField(default=False, verbose_name='Se as narinas estão representadas.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='nariz_boca_duas_dimensoes',
            field=models.BooleanField(default=False, verbose_name='Nariz e boca representados em duas dimensões, os dois lábios indicados.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='nariz_presente',
            field=models.BooleanField(default=False, verbose_name='Se o nariz esta presente.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='olhar',
            field=models.BooleanField(default=False, verbose_name='Representação correta do olhar.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='olhos_detalhados',
            field=models.BooleanField(default=False, verbose_name='Representação das particularidades relativas dos olhos.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='olhos_presentes',
            field=models.BooleanField(default=False, verbose_name='Se os olhos estão presentes.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='olhos_proporcionais',
            field=models.BooleanField(default=False, verbose_name='Olhos proporcionais.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='ombros_definidamente_indicados',
            field=models.BooleanField(default=False, verbose_name='Ombros definidamente indicados.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='oposicao_polegar',
            field=models.BooleanField(default=False, verbose_name='Oposição do polegar, palma da mão representada.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='orelhas',
            field=models.BooleanField(default=False, verbose_name='Representação das orelhas.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='orelhas_proporcionais',
            field=models.BooleanField(default=False, verbose_name='Orelhas proporcionais e colocadas em posições exatas.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='perna_extensao_correta',
            field=models.BooleanField(default=False, verbose_name='Extensão das pernas não menor, nem duas vezes maior que o tronco.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='pernas_presentes',
            field=models.BooleanField(default=False, verbose_name='Se as pernas estão presentes.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='pes_proporcionais',
            field=models.BooleanField(default=False, verbose_name='Pés proporcionais em relação ao corpo.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='pescoco_presente',
            field=models.BooleanField(default=False, verbose_name='Se o pescoço está presente.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='projecao_queixo',
            field=models.BooleanField(default=False, verbose_name='Projeção do queixo representada.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='pupilas',
            field=models.BooleanField(default=False, verbose_name='Representação das pupilas.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='quatro_pecas_de_roupa',
            field=models.BooleanField(default=False, verbose_name='Quatro peças de roupa pelo menos, representadas de modo inequívoco.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='queixo_e_testa',
            field=models.BooleanField(default=False, verbose_name='Representação do queixo e da testa.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='roupa',
            field=models.BooleanField(default=False, verbose_name='Se as roupas esta representada.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='total_numero_de_dedos',
            field=models.BooleanField(default=False, verbose_name='Se o exato numero de dedos está representado.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='tracos_fisionomicos',
            field=models.BooleanField(default=False, verbose_name='Traços fisionõmicos sem nenhuma irregularidade.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='traje_completo',
            field=models.BooleanField(default=False, verbose_name='Traje comleto sem incongruência.'),
        ),
        migrations.AddField(
            model_name='desenhofigurahumana',
            name='tronco_presente',
            field=models.BooleanField(default=False, verbose_name='Se o tronco está presente.'),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='data_anamnese',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data de Anamnese'),
        ),
        migrations.AlterField(
            model_name='conclusao',
            name='data_conclusao',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data da Conclusão'),
        ),
        migrations.AlterField(
            model_name='desenhofigurahumana',
            name='data_avaliacao',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data de Avaliação'),
        ),
        migrations.AlterField(
            model_name='primeiraunidadefuncional',
            name='data_avaliacao',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data de Avaliação'),
        ),
        migrations.AlterField(
            model_name='segundaunidadefuncional',
            name='data_avaliacao',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data de Avaliação'),
        ),
        migrations.AlterField(
            model_name='terceiraunidadefuncional',
            name='data_avaliacao',
            field=models.DateField(default=datetime.date(2022, 8, 4), verbose_name='Data de Avaliação'),
        ),
    ]
