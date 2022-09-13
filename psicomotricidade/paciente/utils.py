import datetime
import pandas as pd
import os
import shutil
from .graficos import *
from .dataframes import unidades_funcionais

# graficos
def separa_por_passagens(df):
    df = df
    df_int = int(df.__len__())

    avaliacoes = []
    for i in df['id']:
        avaliacoes.append(i)

    if df_int <= 1:
        return "Dados insuficientes."

    elif df_int >= 2:
        lista_dfs = []
        for i in avaliacoes:
            df_avaliacoes = df[df['id'] == i]
            df_avaliacoes = df_avaliacoes.drop(columns=['id', 'paciente_id'])
            lista_dfs.append(df_avaliacoes)
        return lista_dfs


def executa_dataframes_e_graficos(id_paciente):
    # excluir e criar a pasta 'media' para alocar as imagens dos graficos
    shutil.rmtree('psicomotricidade/media_graph')
    os.mkdir('psicomotricidade/media_graph')

    # --------------- Gera os Dataframes já filtrados -----------------------
    lista_todos_topicos = unidades_funcionais().topicos(id_paciente)
    # ---------------------------- Primeira Unidade Funcional ----------------------
    # ----------------- TONICIDADE -------------------------------
    relatorio1 = separa_por_passagens(lista_todos_topicos[0])
    relatorio2 = separa_por_passagens(lista_todos_topicos[1])
    # relatorio3 = separa_por_passagens(lista_todos_topicos[2])
    # relatorio4 = separa_por_passagens(lista_todos_topicos[3])
    relatorio5 = separa_por_passagens(lista_todos_topicos[4])
    relatorio6 = separa_por_passagens(lista_todos_topicos[5])
    # ----------------- EQUILIBRAÇÂO -------------------------------
    relatorio7 = separa_por_passagens(lista_todos_topicos[6])
    relatorio8 = separa_por_passagens(lista_todos_topicos[7])
    relatorio9 = separa_por_passagens(lista_todos_topicos[8])
    relatorio10 = separa_por_passagens(lista_todos_topicos[9])

    # ---------------------------- Segunda Unidade Funcional ----------------------
    # ----------------- NOÇÃO CORPORAL -------------------------------
    relatorio11 = separa_por_passagens(lista_todos_topicos[10])
    relatorio12 = separa_por_passagens(lista_todos_topicos[11])
    relatorio14 = separa_por_passagens(lista_todos_topicos[12])
    # ----------------- LATERALIZAÇÕES -------------------------------
    # relatorio15 = separa_por_passagens(lista_todos_topicos[13])
    # relatorio16 = separa_por_passagens(lista_todos_topicos[14])
    # ----------------- ESTRUTURAÇÃO ESPAÇO TEMPORAL -------------------------------
    relatorio17 = separa_por_passagens(lista_todos_topicos[15])
    relatorio18 = separa_por_passagens(lista_todos_topicos[16])
    relatorio19 = separa_por_passagens(lista_todos_topicos[17])
    relatorio20 = separa_por_passagens(lista_todos_topicos[18])

    # ---------------------------- Terceira Unidade Funcional ----------------------
    # ----------------- PRAXIA GLOBAL -------------------------------
    relatorio21 = separa_por_passagens(lista_todos_topicos[19])
    relatorio22 = separa_por_passagens(lista_todos_topicos[20])
    relatorio23 = separa_por_passagens(lista_todos_topicos[21])
    relatorio24 = separa_por_passagens(lista_todos_topicos[22])
    # ----------------- PRAXIA FINA -------------------------------
    relatorio25 = separa_por_passagens(lista_todos_topicos[23])
    relatorio26 = separa_por_passagens(lista_todos_topicos[24])
    relatorio27 = separa_por_passagens(lista_todos_topicos[25])
    # ----------------- GRAFOMOTRICIDADE -------------------------------
    relatorio28 = separa_por_passagens(lista_todos_topicos[26])
    relatorio29 = separa_por_passagens(lista_todos_topicos[27])
    relatorio30 = separa_por_passagens(lista_todos_topicos[28])
    relatorio31 = separa_por_passagens(lista_todos_topicos[29])
    relatorio32 = separa_por_passagens(lista_todos_topicos[30])
    # ----------------- MONTAR QUEBRA-CABEÇA -------------------------------
    relatorio33 = separa_por_passagens(lista_todos_topicos[31])

    # ---------------------------- Desenho da Figura Humana ----------------------
    relatorio13 = separa_por_passagens(lista_todos_topicos[32])

    # ------------- Gera os graficos baseados nos dataframes acima --------------
    graficos = {
        # ---------------------------- Primeira Unidade Funcional ----------------------
        'conceitos_filogeneticos': grafico_de_linha(relatorio1, 'Conceitos Filogenéticos', [1, 2, 3, 4],
                                                    'conceitos_filogeneticos'),

        'extensibilidade': grafico_de_linha(relatorio2, 'Extensibilidade dos Membros',
                                            ['Reduzida', 'Aumentada', 'Normal'], 'extensibilidade'),


        'diadococinesia': grafico_de_linha(relatorio5, 'Diadococinesia', [1, 2, 3, 4], 'diadococinesia'),
        'sincinesia': grafico_de_barra(relatorio6, 'Sincinesia',
                                       ['', 'Nível alto', 'Nível médio', 'Nível baixo', 'Não apresenta'], 'sincinesia'),

        'imobilidade': grafico_de_barra(relatorio7, 'Imobilidade', ['', 'Sem imobilidade',
                                                                    'Imobilidade parcial',
                                                                    'Imobilidade integral'], 'imobilidade'),

        'equilibrio_estatico': grafico_de_barra(relatorio8, 'Equilíbrio Estático',
                                                ['', 'Com dificuldade', '3 segundos', '5 segundos'],
                                                'equilibrio_estatico'),

        'equilibrio_dinamico_ponte': grafico_de_barra(relatorio9, 'Ponte de Equilíbrio', [1, 2, 3, 4],
                                                      'equilibrio_dinamico_ponte'),
        'equilibrio_dinamico_corda': grafico_de_barra(relatorio10, 'Pular corda ', [1, 2, 3, 4],
                                                      'equilibrio_dinamico_corda'),

        # ---------------------------- Segunda Unidade Funcional ----------------------
        'cinestesia': grafico_de_barra_numeros_altos(relatorio11, 'Cinestesia', 'cinestesia'),
        'imitacao_de_gestos': grafico_de_barra_numeros_baixos(relatorio12, 'Imitação de Gestos', 'imitacao_de_gestos'),
        'auto_imagem': grafico_de_barra(relatorio14, 'Auto-Imagem', ['', 'Não possui repertório',
                                                                     'Realizou parcialmente',
                                                                     'Realizou integralmente'], 'auto_imagem'),

        'organizacao_perceptiva': grafico_de_barra(relatorio17, 'Organização Perceptiva', ['', 'Não realizou',
                                                                                           'Realizou parcialmente',
                                                                                           'Realizou integralmente'],
                                                   'organizacao_perceptiva'),
        'estruturacao_dinamica_espacial': grafico_de_barra(relatorio18, 'Estruturação Dinâmica Espacial', ['',
                                                                                                           'Não estruturou',
                                                                                                           'Estruturou parcialmente',
                                                                                                           'Estruturou integralmente'],
                                                           'estruturacao_dinamica_espacial'),
        'representacao_topografica': grafico_de_barra(relatorio19, 'Representação Topográfica', ['', 'Não localizou-se',
                                                                                                 'Localizou-se parcialmente',
                                                                                                 'Localizou-se integralmente'],
                                                      'representacao_topografica'),
        'estruturacao_ritmica': grafico_de_barra_numeros_altos(relatorio20, 'Estruturação Rítmica',
                                                               'estruturacao_ritmica'),

        # ---------------------------- Terceira Unidade Funcional ----------------------
        'oculo_manual': grafico_de_linha(relatorio21, 'Coordenação Óculo-manual',
                                         ['Não realizou', 'Realizou parcialmente', 'Realizou integralmente'],
                                         'oculo_manual'),
        'oculo_pedal': grafico_de_barra(relatorio22, 'Coordenação Óculo-pedal', [-0.5, 0, 1, 2, 3, 4], 'oculo_pedal'),
        'dissociacao': grafico_de_linha(relatorio23, 'Dissociação', [1, 2, 3, 4], 'dissociacao'),
        'agilidade': grafico_de_barra_numeros_baixos(relatorio24, 'Agilidade', 'agilidade'),
        'pulseira_de_clipes': grafico_de_barra_numeros_baixos(relatorio25, 'Pulseira de Clipes', 'pulseira_de_clipes'),
        'tamborilar': grafico_de_barra(relatorio26, 'Tamborilar', ['', 'Não realizou', 'Realizou parcialmente',
                                                                   'Realizou integralmente'], 'tamborilar'),
        'velocidade_precisao': grafico_de_barra_numeros_altos(relatorio27, 'Velocidade e Precisão',
                                                              'velocidade_precisao'),
        'tracados': grafico_de_barra(relatorio28, 'Traçados', [1, 2, 3, 4], 'tracados'),
        'pontilhados': grafico_de_barra(relatorio29, 'Pontilhados', [1, 2, 3, 4], 'pontilhados'),
        'circulos': grafico_de_barra(relatorio30, 'Círculos', [1, 2, 3, 4], 'circulos'),
        'cruz': grafico_de_barra(relatorio31, 'Cruz', [1, 2, 3, 4], 'cruz'),
        'colorir': grafico_de_barra(relatorio32, 'Colorir Graficamente em Diferentes Posições', [1, 2, 3, 4],
                                                   'colorir'),
        'quebra_cabeca': grafico_de_barra(relatorio33, 'Montar Quebra-Cabeça', ['', 'Não realizou',
                                                                                '4 peças', '8 peças', '10 peças'],
                                          'quebra_cabeca'),
        # ---------------------------- Desenho da Figura Humana ----------------------
        'figura_humana': grafico_de_barra_numeros_altos_fig_humana(relatorio13, 'Desenho da Figura Humana', 'figura_humana'),
    }
    return graficos


# tabela goodnough
def tabela_goodnough(data_nascimento, dataframe):
    shutil.rmtree('psicomotricidade/media_goodnough')
    os.mkdir('psicomotricidade/media_goodnough')

    lista_pontuacoes = []
    lista_datas_avaliacoes = []
    for i in dataframe.values:

        pontuacoes = []
        for booleano in i:
            if booleano == True:
                pontuacoes.append(booleano)

        datas_avaliacoes = i[0].strftime("%Y-%m-%d")

        lista_pontuacoes.append(pontuacoes.__len__())
        lista_datas_avaliacoes.append(datas_avaliacoes)

    data_nascimento = data_nascimento
    idades = []
    idades_data_avaliacao = []
    for i in lista_datas_avaliacoes:

        data_nacimento = data_nascimento.toordinal()
        data_atual = datetime.datetime.strptime(i, '%Y-%m-%d').date().toordinal()

        dias = data_atual - data_nacimento

        anos, dias = dias // 365, dias % 365
        meses, dias = dias // 30, dias % 30

        idade_anos = anos
        idade_meses = meses

        # verificar os anos do paciente para enquadrar no padrão da tabela goodnough
        if idade_anos > 13:
            idade_anos = 13
        elif idade_anos < 3:
            idade_anos = 3

        # verificar os meses do paciente para enquadrar no padrão da tabela goodnough
        if (idade_meses == 0) or (idade_meses == 3) or (idade_meses == 6) or (idade_meses == 9):
            idade_meses = idade_meses

        elif idade_meses == 11:
            idade_anos += 1
            idade_meses = 0

        elif idade_meses == 1:
            idade_meses = 0

        elif idade_meses == 2 or idade_meses == 4:
            idade_meses = 3

        elif idade_meses == 5 or idade_meses == 7:
            idade_meses = 6

        elif idade_meses == 8 or idade_meses == 10:
            idade_meses = 9

        idades.append(f'{idade_anos}:{idade_meses}')

        # idade do paciente para apresentação
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

        idades_data_avaliacao.append(idade)

    # tabela goodnough
    tuplas_goodnough = [('3:0', 0), ('3:3', 0), ('3:6', 2), ('3:9', 3), ('4:0', 4), ('4:3', 5), ('4:6', 6), ('4:9', 7),
                        ('5:0', 8), ('5:3', 9), ('5:6', 10), ('5:9', 11), ('6:0', 12), ('6:3', 13), ('6:6', 14),
                        ('6:9', 15), ('7:0', 16), ('7:3', 17), ('7:6', 18), ('7:9', 19), ('8:0', 20), ('8:3', 21),
                        ('8:6', 22), ('8:9', 23), ('9:0', 24), ('9:3', 25), ('9:6', 26), ('9:9', 27), ('10:0', 28),
                        ('10:3', 29), ('10:6', 30), ('10:9', 31), ('11:0', 32), ('11:3', 33), ('11:6', 34),
                        ('11:9', 35), ('12:0', 36), ('12:3', 37), ('12:6', 38), ('12:9', 39), ('13:0', 40),
                        ('13:3', 41), ('13:6', 42), ('13:9', 43)]

    # Gera uma lista com as tuplas referentes as datas cronologicas e pontuaçoes
    tuplas_paciente = []
    count = 0
    for i in idades:
        tupla = (i, lista_pontuacoes[count])
        tuplas_paciente.append(tupla)
        count += 1

    tuplas_e_esperados = []
    for tupla in tuplas_paciente:
        lista_dupla = []
        lista_dupla.append(tupla)
        for tupla_good in tuplas_goodnough:
            if tupla_good[0] == tupla[0]:
                lista_dupla.append(tupla_good)
                tuplas_e_esperados.append(lista_dupla)

    lista_pontuacao_esperada = []
    lista_diferenca = []
    for i in tuplas_e_esperados:
        lista_pontuacao_esperada.append(i[1][1])
        lista_diferenca.append(i[0][1] - i[1][1])

    lista_datas_avaliacoes = lista_datas_avaliacoes
    idades_data_avaliacao = idades_data_avaliacao
    lista_pontuacao_esperada = lista_pontuacao_esperada
    lista_pontuacoes = lista_pontuacoes
    lista_diferenca = lista_diferenca

    lista_de_tuplas = list(
        zip(lista_datas_avaliacoes, idades_data_avaliacao, lista_pontuacao_esperada, lista_pontuacoes, lista_diferenca))

    df = pd.DataFrame(lista_de_tuplas,
                      columns=['Data de Avaliação', 'Idade Cronológica', 'Pontos Esperados',
                               'Pontos Realizados', 'Pontos de Diferença'])

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns),
                    fill_color='WhiteSmoke',
                    align='center',
                ),
                cells=dict(
                    values=[df['Data de Avaliação'], df['Idade Cronológica'], df['Pontos Esperados'],
                            df['Pontos Realizados'], df['Pontos de Diferença']],
                    fill_color='white',
                    align='center',
                )
            )
        ])
    fig.update_traces(
        overwrite=True,
        columnwidth=[8, 12, 7, 7, 8],
        header_line=dict(
            width=2,
            color="WhiteSmoke"
        ),
        header_font=dict(
            size=16,
            color='black',
        ),
        cells_height=30,
        cells_font=dict(
            size=14
        ),
        cells_line=dict(
            width=2,
            color="WhiteSmoke"
        ),
    ),
    fig.update_layout(
        autosize=True,
        title=dict(
            text="Tabela Goodnough",
            font_size=26,
            font_color="black",
            x=0.5,
        ),
        margin=dict(
            b=0
        ),
    )
    fig.write_image("psicomotricidade/media_goodnough/goodnough.webp")
    return fig.to_html(include_plotlyjs='cdn')
