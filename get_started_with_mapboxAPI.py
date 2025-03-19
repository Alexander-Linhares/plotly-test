import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go


from functools import partial
from dotenv import load_dotenv, dotenv_values
from geopy.geocoders import Nominatim
from typing import Tuple, List, Dict
from asyncio import Future, create_task




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

#TOKEN = dotenv_values("./env/.env.secret")["TOKEN"]


#print("Configurações de acesso de API {0}".format(TOKEN))


#configurando o geolocalizador nominatim
geolocator = Nominatim(
    user_agent="Secretaria Municipal da Saúde de Camboriú"
)
#cria uma configuração de função parcial, a função é um callable, enquanto seus keyargs chaves de acesso dos parâmetros da função principal
#resumindo, o primero parâmetro do partial é uma função que será chamda, e os outros argumentos serão 
geocode = partial(geolocator.geocode, language="pt-br")

#shortcut to module map
geolt = go.layout.map
target_city = "Camboriú, Santa Catarina"

"""

    parâmetros
        -> df: é o dataframe de análise
        -> result_type: é o tipo de resultado da notificação:
            NEGATIVO
            CLINICO EPIDEMIOLÓJICO
            AGUARDANDO RESULTADO

    a função get_address_by_result_type faz:
        - filtra o endereço dos casos de agravo onde
        o resultado é igual ao tipo do parâmetro result_type
        -transforma a series em uma lista de endereços
        -cria uma lista de coordenadas
        -percorre cada endereço na lista de endereços de string
        -transforma o endereço de string em um objeto Location
        do módulo geocoders do geopy que possue as coordenadas
        -adiciona o endereço transformado em longitude e latitude
        em uma tupla
        termina o laço e retorna as coordenadas

    falta:

        implementar um async/await para rodar paralelamente ao programa final
        implementar um try except no geocoder (ele é uma api que precisa de internet) pode gerar erro de conexão
"""
def get_address_by_result_type(df: pd.DataFrame, result_type: str) -> pd.DataFrame:
    address_list = df[df["RESULTADO"] == result_type]["ENDEREÇO"]
    coordinates_list = []
    for address in address_list:
        geolocation = geocode(address)
        if geolocation != None:
            coordinates_list.append((
                geolocation.longitude,
                geolocation.latitude))
    
    return pd.DataFrame(
        coordinates_list, 
        columns=['longitude', 'latitude']
    )

    

def display_scatter_map(marker_points=pd.DataFrame):
    cordinates = geocode(target_city)

    #cria o gráfico de disperção
    scattermap = go.Scattermap(
        lat=marker_points['latitude'],
        lon=marker_points['longitude'],
        mode="markers",
        marker=go.scattermap.Marker(
            size=14,
            opacity=0.5,
            color="red"
        ),
        text=["Camboriú"]
    )

    fig = go.Figure(data=scattermap)

    fig.update_layout(
        map=go.layout.Map(
            style="open-street-map",
            center=geolt.Center(
                lat=cordinates.latitude,
                lon=cordinates.longitude
            ),
            zoom=10,
            pitch=0,
            bearing=0,
        )
    )

    fig.show()

if __name__ == "__main__":
    #display_map()
    df = pd.read_excel("./database/db1.xlsx")
    map_points = get_address_by_result_type(df, "CLINICO EPIDEMIOLÓGICO")
    display_scatter_map(map_points)

