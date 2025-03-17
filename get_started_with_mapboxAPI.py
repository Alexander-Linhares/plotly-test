import os
import pandas as pd
import plotly.graph_objects as go


from functools import partial
from dotenv import load_dotenv, dotenv_values
from geopy.geocoders import Nominatim




#df = pd.read_excel("./database/db1.xlsx")

#print(df.columns)

"""
Colunas 

Data, NOTIFICAÇÃO, SINAN, NOME, LOCAL DE NOTIFICAÇÃO,
 ENDEREÇO, RESULTADO, SITUAÇÃO, RECEBIDO, AGENTE, VISITA

tipos de valores para RESULTADO

NEGATIVO
CLINICO EPIDEMIOLÓJICO
AGUARDANDO RESULTADO

"""

TOKEN = dotenv_values("./env/.env.secret")["TOKEN"]


print("Configurações de acesso de API {0}".format(TOKEN))


#configurando o geolocalizador nominatim
geolocator = Nominatim(user_agent="geoDengue")
#cria uma configuração de função parcial, a função é um callable, enquanto seus keyargs chaves de acesso dos parâmetros da função principal
#resumindo, o primero parâmetro do partial é uma função que será chamda, e os outros argumentos serão 
geocode = partial(geolocator.geocode, language="pt-br")

#shortcut to module mapbox
geolt = go.layout.mapbox
target_city = "Camboriú, Santa Catarina"


def print_map():
    cordinates = geocode(target_city)

    #cria o gráfico de disperção
    scattermapbox = go.Scattermapbox(
        lat=[cordinates.latitude],
        lon=[cordinates.longitude],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=14
        ),
        text=["Camboriú"]
    )

    fig = go.Figure(data=scattermapbox)

    fig.update_layout(
        mapbox=go.layout.Mapbox(
            accesstoken=TOKEN,
            style="mapbox://styles/alexander-sms/cm8dj90o800ej01s5g2h1aasb",
            center=geolt.Center(
                lat=cordinates.latitude,
                lon=cordinates.longitue
            )
        )
    )

    fig.show()