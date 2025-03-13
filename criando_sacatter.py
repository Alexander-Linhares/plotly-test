"""
    Figuras no plotly se comportam como objetos JSON,
    porém como dicts do python. plotly é originalmente construído
    em javascript, porém é gerado códigos pythonicos da biblioteca

"""




import plotly.graph_objects as go
from random import randint

length = range(0, 10, 2)
years = [1990 + x for x in length]
sales = [100, 500, 300, 450, 627]

#criamos uma figura e configuramos data para plotar um gráfico de dispersão
fig = go.Figure(data = go.Scatter(x=years, y=sales, mode="markers", marker = dict(
    symbol = "circle",
    size = 10,
    color = "red",
    line = dict(width = 2, color = "black")
)))

#atualizamos o layout
fig.update_layout(
    title = "Vendas durante do mercado de ações",
    xaxis_title = "Anos",
    yaxis_title = "Vendas",
    showlegend = False
)

#podemos criar formas para delimitar áreas
#isso pode ser útil na hora de criar o mapa de calor

"""
    Shapes são formas que delimitama áreas ou explicam nosso gráfico

    alguns parâmetros são interessantes, como:
    type 
        diz o tipo de forma que nosso objeto vai possuir
        é uma String literária, que faz referência a formas
        básicas escritas em inglês
    x0, x1
        diz respeito onde começa e onde termina nosso eixo x do quadrado
    y0, y1
        diz respeito o limite do nosso eixo y em relação ao tamanho vertical do bloco
    fillcolor
        Qual cor queremos que esse bloco possua, pode ser cores em inglês, ou então o padrão
        hexadecimal, ou então no padrão rgb
    opacity
        atributo que configura a opacidade da forma
    line
        line é o mesmo que border, em um dict com especificações de estilo
        assim como width e color
"""

fig.add_shape(
    type = 'rect',
    x0 = 1994, x1 = 1998,
    y0 = 500, y1 = 100,
    fillcolor = "rgb(0, 2, 34)",
    opacity = 0.5,
    line = dict(width=2, color='#f0fd00'),
    label= dict(text='Área de menos quantidade de vendas', font=dict(color="black", size=24)),
)

#utilizamos anotações para modificar a visualizaão de determinado ponto

max_sale = min(sales)
spoted_year_index = sales.index(max_sale)

"""
annotation é outro elemento de construção, seus parâmetros
constroem um objeto e adicionam ele à figure

podemos adicionar quantas anotações quizermos no gráfico

x
    refere-se a qual ponto no gráfico o texto da anotação
    apontará, pode ser um ponto real de alguma seta, ou 
    então qualquer ponto que esteja no parâmetro
y
    mesma coisa que x
text
    configura o texto da anotação, é alinhado no centro
showarrow
    mostra uma seta que aponta para um ponto no gráfico,
    caso for false, ela apenas não mostra a seta que fica na 
    distância do ponto e o texto
arrowhead
    referece a cabeça da seta, no intervalo de 0 a 8, quanto maior
    maior será a distância entre as duas outras semiretas que formam 
    a cabeça de um triângulo aberto em baixo
ax
    distância x do ponto e o label
ay
    distância y do ponto e o label
arrowcolor
    cor da seta
"""

fig.add_annotation(
    x = years[spoted_year_index],
    y = max_sale,
    text = "Highest sales",
    showarrow = True,
    arrowhead = 4,
    ax = -50,
    ay = -50,
    arrowcolor="yellow"
)

fig.show()

