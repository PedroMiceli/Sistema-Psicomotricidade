import plotly.graph_objects as go


def grafico_de_linha(dataframe, nome, ordem, nome_img):
    try:
        categorias = dataframe[0].columns.values

        ordem = ordem
        fig = go.Figure()
        conta = 0
        for i in dataframe:

            valores = None
            for itens in i.values:
                valores = itens

            fig.add_trace(go.Scatter(
                x=categorias,
                y=valores,
                name=f'{conta + 1}ª avaliação'
            ))
            conta += 1

        fig.update_layout(
            autosize=True,
            width=800,
            height=450,
            margin_l=170,
            template='xgridoff',
            margin_r=80,

            legend=dict(
                font_size=15,
            ),

            xaxis=dict(
                showgrid=True,
                showspikes=False,
                ticklabelposition="outside right",
                tickfont=dict(size=12),
            ),

            yaxis=dict(
                showgrid=True,
                tickmode='linear',
                autorange=True,
                categoryorder='array',
                categoryarray=ordem,
                range=[-0.5, 3.5]
            ),

            title=dict(
                font=dict(
                    size=26,
                    color='black'
                ),
                text=f'{nome}'
            )
        )
        fig.plotly_update()
        fig.write_image(f"media_graph/{nome_img}.webp")
        return fig.to_html(include_plotlyjs='cdn')
    except:
        return ""


def grafico_de_barra(dataframe, nome, ordem, nome_img):
    try:
        categorias = dataframe[0].columns.values

        fig = go.Figure()
        conta = 0
        for i in dataframe:

            valores = None
            for itens in i.values:
                valores = itens

            fig.add_trace(go.Bar(
                x=categorias,
                y=valores,
                name=f'{conta + 1}ª avaliação',
                marker={"line": {"width": 3, "color": "rgb(0,0,0)"}}
            ))
            conta += 1

        fig.update_layout(
            autosize=False,
            width=800,
            height=450,
            template='xgridoff',
            margin_l=170,
            bargap=0.30,
            bargroupgap=0.3,

            legend=dict(
                font_size=15,
            ),

            xaxis=dict(
                showgrid=True,
                showspikes=False,

            ),
            xaxis_tickfont=dict(size=18),

            yaxis=dict(
                showgrid=True,
                tickmode='linear',
                autorange=False,
                zeroline=True,
                categoryorder='array',
                categoryarray=ordem,
            ),
            title=dict(
                font=dict(
                    size=26,
                    color='black'
                ),
                text=f'{nome}'
            )
        )

        fig.write_image(f"media_graph/{nome_img}.webp")
        return fig.to_html(include_plotlyjs='cdn')
    except:
        return ""


def grafico_de_barra_numeros_baixos(dataframe, nome, nome_img):
    try:
        categorias = dataframe[0].columns.values

        fig = go.Figure()
        conta = 0
        for i in dataframe:

            valores = None
            for itens in i.values:
                valores = itens

            fig.add_trace(go.Bar(
                x=categorias,
                y=valores,
                name=f'{conta + 1}ª avaliação',
                marker={"line": {"width": 3, "color": "rgb(0,0,0)"}}
            ))
            conta += 1

        fig.update_layout(
            autosize=False,
            width=800,
            height=450,
            template='xgridoff',
            margin_l=170,
            bargap=0.30,
            bargroupgap=0.3,

            legend=dict(
                font_size=15,
            ),

            xaxis=dict(
                showgrid=True,
                showspikes=False,

            ),
            xaxis_tickfont=dict(size=18),
            yaxis=dict(
                showgrid=True,
                dtick=[0, 1]
            ),
            title=dict(
                font=dict(
                    size=26,
                    color='black'
                ),
                text=f'{nome}'
            )
        )

        fig.write_image(f"media_graph/{nome_img}.webp")
        return fig.to_html(include_plotlyjs='cdn')
    except:
        return ""


def grafico_de_barra_numeros_altos(dataframe, nome, nome_img):
    try:
        categorias = dataframe[0].columns.values

        fig = go.Figure()
        conta = 0
        for i in dataframe:

            valores = None
            for itens in i.values:
                valores = itens

            fig.add_trace(go.Bar(
                x=categorias,
                y=valores,
                name=f'{conta + 1}ª avaliação',
                marker={"line": {"width": 3, "color": "rgb(0,0,0)"}}
            ))
            conta += 1

        fig.update_layout(
            autosize=False,
            width=800,
            height=450,
            template='xgridoff',
            margin_l=170,
            bargap=0.30,
            bargroupgap=0.3,

            legend=dict(
                font_size=15,
            ),

            xaxis=dict(
                showgrid=True,
                showspikes=False,

            ),
            xaxis_tickfont=dict(size=18),
            yaxis=dict(
                showgrid=True,
            ),
            title=dict(
                font=dict(
                    size=26,
                    color='black'
                ),
                text=f'{nome}'
            )
        )

        fig.write_image(f"media_graph/{nome_img}.webp")
        return fig.to_html(include_plotlyjs='cdn')
    except:
        return ""


def grafico_de_barra_numeros_altos_fig_humana(dataframe, nome, nome_img):
    try:

        v = []
        c = []

        contador = 0
        for frame in dataframe:
            frame = frame.values
            c.append([f"{contador + 1}ª passagem"])

            for i in frame:

                trues = []
                for valor in i:
                    if valor == True:
                        trues.append(valor)

                inteiro = [int(trues.__len__())]
                v.append(inteiro)
            contador = contador + 1

        fig = go.Figure()

        conta = 0
        for i in v:
            print(conta)
            fig.add_trace(go.Bar(
                x=c[conta],
                y=v[conta],
                name=f'{conta + 1}ª avaliação',
                marker={"line": {"width": 3, "color": "rgb(0,0,0)"}}
            ))
            conta += 1

        fig.update_layout(
            autosize=False,
            width=800,
            height=450,
            template='xgridoff',
            margin_l=170,
            bargap=0.30,
            bargroupgap=0.3,

            legend=dict(
                font_size=15,
            ),

            xaxis=dict(
                showgrid=True,
                showspikes=False,

            ),
            xaxis_tickfont=dict(size=18),
            yaxis=dict(
                showgrid=True,
            ),
            title=dict(
                font=dict(
                    size=26,
                    color='black'
                ),
                text=f'{nome}'
            )
        )

        fig.write_image(f"psicomotricidade/media_graph/{nome_img}.webp")
        return fig.to_html(include_plotlyjs='cdn')
    except:
        return ""

