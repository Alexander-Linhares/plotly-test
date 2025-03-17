"""
    o geobr é uma biblioteca do python que possui geodatasets das localizações oficiais
    do Brasil, como municípios, estados, capitais etc.
    os geodatasets são estruturas de dados que possuem as localizações em formato de latitude e longitude
    que permitirão representar as polígonos do nosso mapa

    por outro lado o geopandas permite a manipulação desses pontos assim como dataframes comuns
    porém voltados a operações de coordenadas
"""

import geobr
import geopandas as gp
import plotly.express as px

muni = geobr.read_municipality(code_muni="SC", year=2022)

gdf = muni[muni.name_muni=="Camboriú"]

