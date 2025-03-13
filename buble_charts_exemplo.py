import plotly.graph_objects as go

"""
o gráfico de disperção em bolha é muito útil ao relacionar 
3 variáveis ao mesmo tempo, lembrando que umas das variáveis 
será o raio da bolha 

cities é o nome de cada bolha no gráfico
"""

cities = ["City A", "City B", "City C"]
population = [500000, 200000, 400000]
temperature = [25, 30, 28]
gdp = [1000000, 200500, 150000]

#Dessa vez o marker recebe um dict diferente
#temos o seguinte:
"""
size
    respectivo ao tamanho da bolha 
"""
fig = go.Figure(data = go.Scatter(
    x=cities, 
    y=population, 
    mode="markers",
    marker = dict(
            size = gdp,
            sizemode = "area",
            sizeref = max(gdp) / 100,
            sizemin = 2,
            color = "blue",
            showscale = True
        ),
        text=cities
    )
)

fig.show()