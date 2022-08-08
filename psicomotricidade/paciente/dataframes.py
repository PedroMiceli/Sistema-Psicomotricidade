import pandas as pd
from sqlalchemy import create_engine
import json



def df_unidades():

    def ler_json():
        with open("./keys.json", 'r', encoding='utf8') as f:
            return json.load(f)

    chaves = ler_json()
    driver = chaves["driver"]
    usuario = chaves["usuario"]
    senha = chaves["senha"]
    ip = chaves["ip"]
    porta = chaves["porta"]
    banco = chaves["banco"]

    senha = f"{driver}://{usuario}:{senha}@{ip}:{porta}/{banco}"

    engine = create_engine(senha).connect()

    df_primeira_unidade = pd.read_sql_table('primeira_unidade_funcional', engine)
    df_primeira_unidade = df_primeira_unidade.sort_values(by='id')

    df_segunda_unidade = pd.read_sql_table('segunda_unidade_funcional', engine)
    df_segunda_unidade = df_segunda_unidade.sort_values(by='id')

    df_terceira_unidade = pd.read_sql_table('terceira_unidade_funcional', engine)
    df_terceira_unidade = df_terceira_unidade.sort_values(by='id')

    df_figura_humana = pd.read_sql_table('desenhos_figura_humana', engine)
    df_figura_humana = df_figura_humana.sort_values(by='id')

    lista = [df_primeira_unidade, df_segunda_unidade, df_terceira_unidade, df_figura_humana]
    return lista


class unidades_funcionais():

    def topicos(self, id_paciente):
        while True:
            unidades = df_unidades()
            lista_todos_topicos = []

            # ----------------- Primeira Unidade Funcional------------------
            # ----------------- Tonicidade ----------------------
            df_conceitos_filogeneticos = unidades[0][['id', 'paciente_id', 'rolar', 'engatinhar', 'rastejar']]
            df_conceitos_filogeneticos.columns = ['id', 'paciente_id', 'Rolar', 'Engatinhar', 'Rastejar']
            df_conceitos_filogeneticos = df_conceitos_filogeneticos[
                df_conceitos_filogeneticos['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_conceitos_filogeneticos)

            df_extensibilidade = unidades[0][['id', 'paciente_id', 'extensibilidade_membros_superiores',
                                              'extensibilidade_membros_inferiores']]
            df_extensibilidade.columns = ['id', 'paciente_id', 'Membros superiores', 'Membros inferiores']
            df_extensibilidade = df_extensibilidade[df_extensibilidade['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_extensibilidade)

            df_balanco_passivo = unidades[0][['id', 'paciente_id', 'balanco_membros_superiores']]
            df_balanco_passivo.columns = ['id', 'paciente_id', 'Membros superiores']
            df_balanco_passivo = df_balanco_passivo[df_balanco_passivo['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_balanco_passivo)

            df_paratonia = unidades[0][['id', 'paciente_id', 'paratonia_membros_superiores']]
            df_paratonia.columns = ['id', 'paciente_id', 'Membros superiores']
            df_paratonia = df_paratonia[df_paratonia['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_paratonia)

            df_diadococinesia = unidades[0][['id', 'paciente_id', 'pronacao', 'supinacao']]
            df_diadococinesia.columns = ['id', 'paciente_id', 'Pronação', 'Supinação']
            df_diadococinesia = df_diadococinesia[df_diadococinesia['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_diadococinesia)

            df_sincinesia = unidades[0][['id', 'paciente_id', 'tonico', 'tonico_cinetico']]
            df_sincinesia.columns = ['id', 'paciente_id', 'Tônico', 'Tônico-cinético']
            df_sincinesia = df_sincinesia[df_sincinesia['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_sincinesia)

            # ----------------- Equilibração -------------------------------
            df_imobilidade = unidades[0][['id', 'paciente_id', 'imobilidade']]
            df_imobilidade.columns = ['id', 'paciente_id', 'Imobilidade']
            df_imobilidade = df_imobilidade[df_imobilidade['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_imobilidade)

            df_equilibrio_estatico = unidades[0][['id', 'paciente_id', 'equilibrio_estatico']]
            df_equilibrio_estatico.columns = ['id', 'paciente_id', 'Equilibrio estático']
            df_equilibrio_estatico = df_equilibrio_estatico[df_equilibrio_estatico['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_equilibrio_estatico)

            df_equilibrio_dinamico_ponte = unidades[0][['id', 'paciente_id', 'ponte_equilibrio_frente',
                                                        'ponte_equilibrio_tras', 'ponte_equilibrio_direita',
                                                        'ponte_equilibrio_esquerda']]
            df_equilibrio_dinamico_ponte.columns = ['id', 'paciente_id', 'Frente', 'Trás', 'Direita', 'Esquerda']
            df_equilibrio_dinamico_ponte = df_equilibrio_dinamico_ponte[
                df_equilibrio_dinamico_ponte['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_equilibrio_dinamico_ponte)

            df_equilibrio_dinamico_corda = unidades[0][
                ['id', 'paciente_id', 'corda_olhos_abertos', 'corda_olhos_fechados']]
            df_equilibrio_dinamico_corda.columns = ['id', 'paciente_id', 'Olhos abertos', 'Olhos fechados']
            df_equilibrio_dinamico_corda = df_equilibrio_dinamico_corda[
                df_equilibrio_dinamico_corda['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_equilibrio_dinamico_corda)

            # -----------------Segunda Unidade Funcional------------------
            # ----------------- Noção Corporal ----------------------

            df_cinestesia = unidades[1][['id', 'paciente_id', 'nomeia_pontos_tateis']]
            df_cinestesia.columns = ['id', 'paciente_id', 'Nomeia pontos táteis do corpo']
            df_cinestesia = df_cinestesia[df_cinestesia['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_cinestesia)

            df_imitacao_de_gestos = unidades[1][['id', 'paciente_id', 'imitacao_de_gestos']]
            df_imitacao_de_gestos.columns = ['id', 'paciente_id', 'Imitação de gestos']
            df_imitacao_de_gestos = df_imitacao_de_gestos[df_imitacao_de_gestos['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_imitacao_de_gestos)

            df_auto_imagem = unidades[1][['id', 'paciente_id', 'no_avaliador', 'no_mesmo', 'no_objeto']]
            df_auto_imagem.columns = ['id', 'paciente_id', 'No avaliador', 'No mesmo', 'No objeto']
            df_auto_imagem = df_auto_imagem[df_auto_imagem['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_auto_imagem)

            # ----------------- Lateralização ----------------------
            df_lateralizacoes = unidades[1][['id', 'paciente_id', 'lateralizacao_ocular',
                                             'lateralizacao_manual', 'lateralizacao_pedal']]
            df_lateralizacoes.columns = ['id', 'paciente_id', 'Lateralização ocular', 'Lateralização manual',
                                         'Lateralização pedal']
            df_lateralizacoes = df_lateralizacoes[df_lateralizacoes['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_lateralizacoes)

            df_reconhecimento_direita_esquerda = unidades[1][['id', 'paciente_id', 'reconhecimento_verbal',
                                                              'reconhecimento_gestual', 'reconhecimento_tatil']]
            df_reconhecimento_direita_esquerda.columns = ['id', 'paciente_id', 'Reconhecimento verbal',
                                                          'Reconhecimento gestual', 'Reconhecimento tátil']
            df_reconhecimento_direita_esquerda = df_reconhecimento_direita_esquerda[
                df_reconhecimento_direita_esquerda['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_reconhecimento_direita_esquerda)

            # ----------------- Estruturação Espaço Temporal ----------------------
            df_organizacao_perceptiva = unidades[1][['id', 'paciente_id', 'organizacao_perceptiva']]
            df_organizacao_perceptiva.columns = ['id', 'paciente_id', 'Organização perceptiva']
            df_organizacao_perceptiva = df_organizacao_perceptiva[
                df_organizacao_perceptiva['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_organizacao_perceptiva)

            df_estruturacao_dinamica_espacial = unidades[1][['id', 'paciente_id', 'estruturacao_dinamica_espacial']]
            df_estruturacao_dinamica_espacial.columns = ['id', 'paciente_id', 'Estruturação dinâmica espacial']
            df_estruturacao_dinamica_espacial = df_estruturacao_dinamica_espacial[
                df_estruturacao_dinamica_espacial['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_estruturacao_dinamica_espacial)

            df_representacao_topografica = unidades[1][['id', 'paciente_id', 'representacao_topografica']]
            df_representacao_topografica.columns = ['id', 'paciente_id', 'Representação topográfica']
            df_representacao_topografica = df_representacao_topografica[
                df_representacao_topografica['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_representacao_topografica)

            df_estruturacao_ritmica = unidades[1][
                ['id', 'paciente_id', 'codificacao', 'decodificacao', 'transcodificacao_auditiva',
                 'transcodificacao_visual']]
            df_estruturacao_ritmica.columns = ['id', 'paciente_id', 'Codificar', 'Decodificar', 'Auditiva', 'Visual']
            df_estruturacao_ritmica = df_estruturacao_ritmica[df_estruturacao_ritmica['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_estruturacao_ritmica)

            # ---------------------------- Terceira Unidade Funcional ----------------------
            # ----------------- Praxia Global -------------------------------
            df_coordenacao_oculo_manual = unidades[2][
                ['id', 'paciente_id', 'jogar_quatro_bolas', 'agarrar_bola_de_tenis']]
            df_coordenacao_oculo_manual.columns = ['id', 'paciente_id', 'Jogar 4 bolas', 'Agarrar bola de tênis']
            df_coordenacao_oculo_manual = df_coordenacao_oculo_manual[
                df_coordenacao_oculo_manual['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_coordenacao_oculo_manual)

            df_coordenacao_oculo_pedal = unidades[2][['id', 'paciente_id', 'quatro_chutes_ao_gol']]
            df_coordenacao_oculo_pedal.columns = ['id', 'paciente_id', '4 chutes ao gol']
            df_coordenacao_oculo_pedal = df_coordenacao_oculo_pedal[
                df_coordenacao_oculo_pedal['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_coordenacao_oculo_pedal)

            df_dissociacao = unidades[2][['id', 'paciente_id', 'dissociacao_membros_superiores',
                                          'dissociacao_membros_inferiores']]
            df_dissociacao.columns = ['id', 'paciente_id', 'Membros superiores', 'Membros inferiores']
            df_dissociacao = df_dissociacao[df_dissociacao['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_dissociacao)

            df_agilidade = unidades[2][['id', 'paciente_id', 'agilidade']]
            df_agilidade.columns = ['id', 'paciente_id', 'Agilidade']
            df_agilidade = df_agilidade[df_agilidade['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_agilidade)

            # ----------------- Praxia Fina ----------------------
            df_pulseira_de_clipes = unidades[2][['id', 'paciente_id', 'pulseira_de_clipes']]
            df_pulseira_de_clipes.columns = ['id', 'paciente_id', 'Pulseira de clipes']
            df_pulseira_de_clipes = df_pulseira_de_clipes[df_pulseira_de_clipes['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_pulseira_de_clipes)

            df_tamborilar = unidades[2][['id', 'paciente_id', 'tamborilar']]
            df_tamborilar.columns = ['id', 'paciente_id', 'Tamborilar']
            df_tamborilar = df_tamborilar[df_tamborilar['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_tamborilar)

            df_velocidade_precisao = unidades[2][['id', 'paciente_id', 'velocidade_precisao']]
            df_velocidade_precisao.columns = ['id', 'paciente_id', 'Velocidade e Precisão']
            df_velocidade_precisao = df_velocidade_precisao[df_velocidade_precisao['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_velocidade_precisao)

            # ----------------- Grafomotricidade ----------------------
            df_tracados = unidades[2][['id', 'paciente_id', 'tracado_vertical', 'tracado_horizontal',
                                       'tracado_zig_zag', 'tracado_curvo']]
            df_tracados.columns = ['id', 'paciente_id', 'Vertical', 'Horizontal', 'Zig-zag', 'Curvo']
            df_tracados = df_tracados[df_tracados['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_tracados)

            df_pontilhados = unidades[2][['id', 'paciente_id', 'pontilhados']]
            df_pontilhados.columns = ['id', 'paciente_id', 'Pontilhados']
            df_pontilhados = df_pontilhados[df_pontilhados['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_pontilhados)

            df_circulos = unidades[2][['id', 'paciente_id', 'circulos']]
            df_circulos.columns = ['id', 'paciente_id', 'Círculos']
            df_circulos = df_circulos[df_circulos['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_circulos)

            df_cruz = unidades[2][['id', 'paciente_id', 'cruz']]
            df_cruz.columns = ['id', 'paciente_id', 'Cruz']
            df_cruz = df_cruz[df_cruz['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_cruz)

            df_colorir = unidades[2][['id', 'paciente_id', 'colorir_graficamente']]
            df_colorir.columns = ['id', 'paciente_id', 'Colorir graficamente']
            df_colorir = df_colorir[df_colorir['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_colorir)

            # ----------------- Montar Quebra-Cabeça ----------------------
            df_montar_quebra_cabeca = unidades[2][['id', 'paciente_id', 'montar_quebra_cabeca']]
            df_montar_quebra_cabeca.columns = ['id', 'paciente_id', 'Montar quebra-cabeça']
            df_montar_quebra_cabeca = df_montar_quebra_cabeca[df_montar_quebra_cabeca['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_montar_quebra_cabeca)

            # ---------------------------- Desenho Figura Humana ----------------------
            # ----------------- Figura Humana -------------------------------
            df_desenho_figura_humana = unidades[3][['id', 'paciente_id', 'cabeca_presente','pernas_presentes','bracos_presentes','tronco_presente',
                                                    'comprimento_do_tronco_maior_que_largura','ombros_definidamente_indicados','bracos_pernas_ligados_ou_tronco',
                                                    'bracos_pernas_ligados_ou_tronco_lugares_convenientes','pescoco_presente','contorno_do_pescoco_continuado',
                                                    'olhos_presentes',
                                                    'nariz_presente','boca_presente','nariz_boca_duas_dimensoes','narinas','cabelos',
                                                    'cabelos_contorno_cabeca','roupa','duas_pecas_de_roupas','desenho_sem_transparencia','quatro_pecas_de_roupa',
                                                    'traje_completo','dedos_da_mao','total_numero_de_dedos','dedos_corretos','oposicao_polegar',
                                                    'maos_distinta_do_braco','juntas_membros_sup','juntas_membros_inf','cabeca_tamanho_correto',
                                                    'bracos_extensao_correta','perna_extensao_correta','pes_proporcionais','bracos_e_pernas_proporcionais',
                                                    'calcanhares','linhas_firmes','linhas_tracadas_e_firmes','contorno_cabeca',
                                                    'contorno_tronco','contorno_bracos','tracos_fisionomicos','orelhas','orelhas_proporcionais','olhos_detalhados',
                                                    'pupilas','olhos_proporcionais','olhar','queixo_e_testa','projecao_queixo','corpo_em_perfil_transparencia',
                                                    'corpo_em_perfil_sem_transparencia',]]


            df_desenho_figura_humana = df_desenho_figura_humana[df_desenho_figura_humana['paciente_id'] == id_paciente]
            lista_todos_topicos.append(df_desenho_figura_humana)

            df_desenho_figura_humana_goodnough = unidades[3][['id', 'paciente_id','data_avaliacao', 'cabeca_presente','pernas_presentes','bracos_presentes','tronco_presente',
                                                    'comprimento_do_tronco_maior_que_largura','ombros_definidamente_indicados','bracos_pernas_ligados_ou_tronco',
                                                    'bracos_pernas_ligados_ou_tronco_lugares_convenientes','pescoco_presente','contorno_do_pescoco_continuado',
                                                    'olhos_presentes',
                                                    'nariz_presente','boca_presente','nariz_boca_duas_dimensoes','narinas','cabelos',
                                                    'cabelos_contorno_cabeca','roupa','duas_pecas_de_roupas','desenho_sem_transparencia','quatro_pecas_de_roupa',
                                                    'traje_completo','dedos_da_mao','total_numero_de_dedos','dedos_corretos','oposicao_polegar',
                                                    'maos_distinta_do_braco','juntas_membros_sup','juntas_membros_inf','cabeca_tamanho_correto',
                                                    'bracos_extensao_correta','perna_extensao_correta','pes_proporcionais','bracos_e_pernas_proporcionais',
                                                    'calcanhares','linhas_firmes','linhas_tracadas_e_firmes','contorno_cabeca',
                                                    'contorno_tronco','contorno_bracos','tracos_fisionomicos','orelhas','orelhas_proporcionais','olhos_detalhados',
                                                    'pupilas','olhos_proporcionais','olhar','queixo_e_testa','projecao_queixo','corpo_em_perfil_transparencia',
                                                    'corpo_em_perfil_sem_transparencia',]]

            df_desenho_figura_humana_goodnough = df_desenho_figura_humana_goodnough[
                df_desenho_figura_humana_goodnough['paciente_id'] == id_paciente]
            df_desenho_figura_humana_goodnough = df_desenho_figura_humana_goodnough.drop(columns=['id', 'paciente_id'])
            lista_todos_topicos.append(df_desenho_figura_humana_goodnough)

            return lista_todos_topicos
