import json
from .dataframes import df_unidades
import statistics


class relatorio():
    # ---------------------- JSON ----------------------
    def ler_json(self):
        try:
            with open("psicomotricidade/paciente/textos_relatorio.json", 'r', encoding="utf-8") as f:
                return json.load(f)
        except:
            return ""

    def df_unidade_relatorio(self, id_paciente):
        while True:
            unidades = df_unidades()

            # ----------------- Primeira Unidade Funcional -----------------
            # ----------------- Tonicidade -----------------
            def conceitos_filogeneticos(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def extensibilidade(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Reduzida":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Aumentada":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Normal":
                        lista_resultados_em_numeros.append(2)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def balanco_passivo(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Movimentos pendulares":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Apresenta resistência":
                        lista_resultados_em_numeros.append(1)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def paratonia(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Sem paratonia":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Com paratonia":
                        lista_resultados_em_numeros.append(1)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def diadococinesia(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def sincinesia(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Nível alto":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Nível médio":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Nível baixo":
                        lista_resultados_em_numeros.append(3)
                    elif i == "Não apresenta":
                        lista_resultados_em_numeros.append(4)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Equilibração -----------------
            def imobilidade(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Sem imobilidade":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Imobilidade parcial":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Imobilidade integral":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def equilibrio_estatico(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Com dificuldade":
                        lista_resultados_em_numeros.append(1)
                    elif i == "3 segundos":
                        lista_resultados_em_numeros.append(2)
                    elif i == "5 segundos":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def equilibrio_dinamico(id_paciente, objetivo, topico, campo):
                df = unidades[0][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['primeira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Segunda Unidade Funcional -----------------
            # ----------------- Noção Corporal -----------------
            def cinestesia(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def imitacao_de_gestos(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def auto_imagem(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não possui repertório":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Realizou parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Realizou integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Lateralização -----------------
            def lateralizacoes(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Indefinida":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Esquerda":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Direita":
                        lista_resultados_em_numeros.append(1)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def reconhecimento_direita_esquerda(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não reconheceu":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Reconhecimento parcial":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Reconhecimento integral":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Estruturação Espaço Temporal -----------------
            def organizacao_perceptiva(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não realizou":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Realizou parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Realizou integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def estruturacao_dinamica_espacial(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não estruturou":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Estruturou parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Estruturou integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def representacao_topografica(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não localizou-se":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Localizou-se parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Localizou-se integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def estruturacao_ritmica(id_paciente, objetivo, topico, campo):
                df = unidades[1][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['segunda_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Terceira Unidade Funcional -----------------
            # ----------------- Praxia Global -----------------
            def coordenacao_oculo_manual(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não realizou":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Realizou parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Realizou integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def coordenacao_oculo_pedal(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def dissociacao(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def agilidade(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Praxia Fina -----------------
            def pulseira_de_clipes(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def tamborilar(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                # resultados do banco
                lista_resultados = []
                if df[f'{campo}'].__len__() == 0:
                    lista_resultados.append("")
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(i)

                # converter os resultados do banco em valores numericos
                lista_resultados_em_numeros = []
                for i in lista_resultados:
                    if i == "Não realizou":
                        lista_resultados_em_numeros.append(1)
                    elif i == "Realizou parcialmente":
                        lista_resultados_em_numeros.append(2)
                    elif i == "Realizou integralmente":
                        lista_resultados_em_numeros.append(3)
                    else:
                        lista_resultados_em_numeros.append("")

                # calcular a média e inserir um texto referente a média e o resultado da ultima avaliação
                media = None
                resultado_json = None
                if lista_resultados[0] != "":
                    media = round(statistics.mean(lista_resultados_em_numeros), 2)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{lista_resultados[0]}']

                texto = None
                if lista_resultados_em_numeros[0] == "":
                    texto = ["", ""]
                elif lista_resultados_em_numeros[0] > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif lista_resultados_em_numeros[0] == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            def velocidade_precisao(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            # ----------------- Grafomotricidade -----------------
            def grafomotricidade(id_paciente, objetivo, topico, campo):
                df = unidades[2][['id', 'paciente_id', 'data_avaliacao', f'{campo}']]
                df = df[df['paciente_id'] == id_paciente]
                df = df.sort_values(by='data_avaliacao', ascending=False)

                media = None
                ultimo_resultado = None
                resultado_json = None
                lista_resultados = []

                if df[f'{campo}'].__len__() == 0:
                    pass
                else:
                    for i in df[f'{campo}']:
                        lista_resultados.append(int(i))

                    media = round(statistics.mean(lista_resultados), 2)
                    ultimo_resultado = df[f'{campo}'].iloc[0]
                    ultimo_resultado = int(ultimo_resultado)

                    json = self.ler_json()
                    resultado_json = json['terceira_unidade'][f'{objetivo}'][f'{topico}'][f'{campo}'][
                        f'{ultimo_resultado}']

                texto = None
                if ultimo_resultado is None:
                    texto = ["", ""]
                elif ultimo_resultado > media:
                    texto = ["Neste fator psicomotor nota-se avanços obtidos pelo paciente.", resultado_json]
                elif ultimo_resultado == media:
                    texto = ["Neste fator psicomotor o paciente encontra-se em processo de aquisição da habilidade.",
                             resultado_json]
                else:
                    texto = ["Neste fator psicomotor o paciente ainda necessita de estimulação.", resultado_json]

                return texto

            resultados = {
                # ---------- Primeira Unidade Funcional ----------
                # ---------- conceitos filogeneticos ----------
                'rolar': conceitos_filogeneticos(id_paciente, 'tonicidade',
                                                 'conceitos_filogeneticos', 'rolar'),
                'engatinhar': conceitos_filogeneticos(id_paciente, 'tonicidade', 'conceitos_filogeneticos',
                                                      'engatinhar'),
                'rastejar': conceitos_filogeneticos(id_paciente, 'tonicidade', 'conceitos_filogeneticos',
                                                    'rastejar'),

                # ---------- extensibilidade ----------
                'extensibilidade_membros_superiores': extensibilidade(id_paciente, 'tonicidade',
                                                                      'extensibilidade',
                                                                      'extensibilidade_membros_superiores'),
                'extensibilidade_membros_inferiores': extensibilidade(id_paciente, 'tonicidade',
                                                                      'extensibilidade',
                                                                      'extensibilidade_membros_inferiores'),

                # ---------- balanço passivo ----------
                'balanco_membros_superiores': balanco_passivo(id_paciente, 'tonicidade', 'balanco_passivo',
                                                              'balanco_membros_superiores'),
                # ---------- paratonia ----------
                'paratonia_membros_superiores': paratonia(id_paciente, 'tonicidade', 'paratonia',
                                                          'paratonia_membros_superiores'),

                # ---------- diadococinesia ----------
                'pronacao': diadococinesia(id_paciente, 'tonicidade', 'diadococinesia', 'pronacao'),
                'supinacao': diadococinesia(id_paciente, 'tonicidade', 'diadococinesia', 'supinacao'),

                # ---------- sincinesia ----------
                'tonico': sincinesia(id_paciente, 'tonicidade', 'sincinesia', 'tonico'),

                'tonico_cinetico': sincinesia(id_paciente, 'tonicidade', 'sincinesia', 'tonico_cinetico'),

                # ---------- imobilidade ----------
                'imobilidade': imobilidade(id_paciente, 'equilibracao', 'imobilidade', 'imobilidade'),

                # ---------- equilibrio estatico ----------
                'equilibrio_estatico': equilibrio_estatico(id_paciente, 'equilibracao',
                                                           'equilibrio_estatico',
                                                           'equilibrio_estatico'),

                # ---------- equilibrio dinamico ----------
                'ponte_equilibrio_frente': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                               'equilibrio_dinamico',
                                                               'ponte_equilibrio_frente'),

                'ponte_equilibrio_tras': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                             'equilibrio_dinamico',
                                                             'ponte_equilibrio_tras'),

                'ponte_equilibrio_direita': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                                'equilibrio_dinamico',
                                                                'ponte_equilibrio_direita'),

                'ponte_equilibrio_esquerda': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                                 'equilibrio_dinamico',
                                                                 'ponte_equilibrio_esquerda'),

                'corda_olhos_abertos': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                           'equilibrio_dinamico',
                                                           'corda_olhos_abertos'),

                'corda_olhos_fechados': equilibrio_dinamico(id_paciente, 'equilibracao',
                                                            'equilibrio_dinamico',
                                                            'corda_olhos_fechados'),
                # ---------- Segunda Unidade Funcional ----------
                # ---------- cinestesia ----------
                'nomeia_pontos_tateis': cinestesia(id_paciente, 'nocao_corporal', 'cinestesia',
                                                   'nomeia_pontos_tateis'),

                # ---------- imitacao de gestos ----------
                'imitacao_de_gestos': imitacao_de_gestos(id_paciente, 'nocao_corporal',
                                                         'imitacao_de_gestos',
                                                         'imitacao_de_gestos'),

                # ---------- auto-imagem ----------
                'avaliador': auto_imagem(id_paciente, 'nocao_corporal', 'auto_imagem', 'no_avaliador'),

                'em_si': auto_imagem(id_paciente, 'nocao_corporal', 'auto_imagem', 'no_mesmo'),

                'objeto': auto_imagem(id_paciente, 'nocao_corporal', 'auto_imagem', 'no_objeto'),

                # ---------- lateralizações ----------
                'lateralizacao_ocular': lateralizacoes(id_paciente, 'lateralizacao', 'lateralizacoes',
                                                       'lateralizacao_ocular'),

                'lateralizacao_manual': lateralizacoes(id_paciente, 'lateralizacao', 'lateralizacoes',
                                                       'lateralizacao_manual'),

                'lateralizacao_pedal': lateralizacoes(id_paciente, 'lateralizacao', 'lateralizacoes',
                                                      'lateralizacao_pedal'),

                # ---------- reconhecimento direita/esquerda ----------
                'reconhecimento_verbal': reconhecimento_direita_esquerda(id_paciente, 'lateralizacao',
                                                                         'reconhecimento_direita_esquerda',
                                                                         'reconhecimento_verbal'),

                'reconhecimento_gestual': reconhecimento_direita_esquerda(id_paciente, 'lateralizacao',
                                                                          'reconhecimento_direita_esquerda',
                                                                          'reconhecimento_gestual'),

                'reconhecimento_tatil': reconhecimento_direita_esquerda(id_paciente, 'lateralizacao',
                                                                        'reconhecimento_direita_esquerda',
                                                                        'reconhecimento_tatil'),

                # ---------- organização perceptiva ----------
                'organizacao_perceptiva': organizacao_perceptiva(id_paciente,
                                                                 'estruturacao_espaco_temporal',
                                                                 'organizacao_perceptiva',
                                                                 'organizacao_perceptiva'),

                # ---------- estruturação dinamica espacial ----------
                'estruturacao_dinamica': estruturacao_dinamica_espacial(id_paciente,
                                                                        'estruturacao_espaco_temporal',
                                                                        'estruturacao_dinamica_espacial',
                                                                        'estruturacao_dinamica_espacial'),

                # ---------- representação topografica ----------
                'representacao_topografica': representacao_topografica(id_paciente,
                                                                       'estruturacao_espaco_temporal',
                                                                       'representacao_topografica',
                                                                       'representacao_topografica'),

                # ---------- estruturação ritmica ----------
                'codificacao': estruturacao_ritmica(id_paciente, 'estruturacao_espaco_temporal',
                                                    'estruturacao_ritmica', 'codificacao'),

                'decodificacao': estruturacao_ritmica(id_paciente, 'estruturacao_espaco_temporal',
                                                      'estruturacao_ritmica', 'decodificacao'),

                'transcodificacao_auditiva': estruturacao_ritmica(id_paciente,
                                                                  'estruturacao_espaco_temporal',
                                                                  'estruturacao_ritmica',
                                                                  'transcodificacao_auditiva'),

                'transcodificacao_visual': estruturacao_ritmica(id_paciente, 'estruturacao_espaco_temporal',
                                                                'estruturacao_ritmica',
                                                                'transcodificacao_visual'),

                # ---------- Terceira Unidade Funcional ----------
                # ---------- coordenação oculo-manual ----------
                'jogar_quatro_bolas': coordenacao_oculo_manual(id_paciente, 'praxia_global',
                                                               'coordenacao_oculo_manual',
                                                               'jogar_quatro_bolas'),
                'agarrar_bola_de_tenis': coordenacao_oculo_manual(id_paciente, 'praxia_global',
                                                                  'coordenacao_oculo_manual',
                                                                  'agarrar_bola_de_tenis'),

                # ---------- coordenação oculo-pedal ----------
                'quatro_chutes_ao_gol': coordenacao_oculo_pedal(id_paciente, 'praxia_global',
                                                                'coordenacao_oculo_pedal',
                                                                'quatro_chutes_ao_gol'),

                # ---------- dissociação ----------
                'dissociacao_membros_superiores': dissociacao(id_paciente, 'praxia_global',
                                                              'dissociacao',
                                                              'dissociacao_membros_superiores'),

                'dissociacao_membros_inferiores': dissociacao(id_paciente, 'praxia_global',
                                                              'dissociacao',
                                                              'dissociacao_membros_inferiores'),

                # ---------- agilidade ----------
                'agilidade': agilidade(id_paciente, 'praxia_global', 'agilidade', 'agilidade'),

                # ---------- pulseira de clipes ----------
                'pulseira_de_clipes': pulseira_de_clipes(id_paciente, 'praxia_fina', 'pulseira_de_clipes',
                                                         'pulseira_de_clipes'),

                # ---------- tamborilar ----------
                'tamborilar': tamborilar(id_paciente, 'praxia_fina', 'tamborilar', 'tamborilar'),

                # ---------- velocidade e precisão ----------
                'velocidade_precisao': velocidade_precisao(id_paciente, 'praxia_fina',
                                                           'velocidade_precisao',
                                                           'velocidade_precisao'),

                # ---------- traçados ----------
                'tracado_vertical': grafomotricidade(id_paciente, 'grafomotricidade', 'tracados',
                                                     'tracado_vertical'),

                'tracado_horizontal': grafomotricidade(id_paciente, 'grafomotricidade', 'tracados',
                                                       'tracado_horizontal'),

                'tracado_zig_zag': grafomotricidade(id_paciente, 'grafomotricidade', 'tracados',
                                                    'tracado_zig_zag'),

                'tracado_curvo': grafomotricidade(id_paciente, 'grafomotricidade', 'tracados',
                                                  'tracado_curvo'),

                # ---------- pontilhados ----------
                'pontilhados': grafomotricidade(id_paciente, 'grafomotricidade', 'pontilhados',
                                                'pontilhados'),

                # ---------- circulos ----------
                'circulos': grafomotricidade(id_paciente, 'grafomotricidade', 'circulos', 'circulos'),

                # ---------- cruz ----------
                'cruz': grafomotricidade(id_paciente, 'grafomotricidade', 'cruz', 'cruz'),

                # ---------- colorir ----------
                'colorir_graficamente': grafomotricidade(id_paciente, 'grafomotricidade', 'colorir',
                                                         'colorir_graficamente'),

                # ---------- Figura Humana ----------
                 #'desenho_figura_humana': figura_humana(paciente_id),
            }
            return resultados
