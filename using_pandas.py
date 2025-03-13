import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Nomes": ["Walter", "Marcelo", "Roberto", "Carlos", "Antônio", "José", "Maria"],
    "Idades": [20, 23, 40, 12, 45, 80, 7],
    "Medias": [6.3, 7, 6.0, 8.9, 10, 5.7, 9.2]
})

fig = px.bar(
    df, 
    x='Idades',
    y='Medias', 
    text='Nomes'
)

#aí vc descobre que não tá entendo nada 

fig.show()