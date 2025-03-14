import plotly.express as px
import pandas as pd
import numpy as np
from functools import partial
from geopy.geocoders import Nominatim


df = pd.read_excel("./database/db1.xlsx")

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

#configurando o geolocalizador nominatim
geolocator = Nominatim(user_agent="geoDengue")
#cria uma configuração de função parcial, a função é um callable, enquanto seus keyargs chaves de acesso dos parâmetros da função principal
geocode = partial(geolocator.geocode, language="pt-br")

#seleciona uma series dos endereços, onde os resultados são clinico epidemiológico
aggravation_case_addresses = df[df["RESULTADO"] == "CLINICO EPIDEMIOLÓGICO"]["ENDEREÇO"]

print(df.groupby([aggravation_case_addresses, "LOCAL DE NOTIFICAÇÃO"])["RESULTADO"].count())


target_city = "Camboriú, Santa Catarina"
cordinates = geocode(target_city)

print(cordinates.latitude, cordinates.longitude)