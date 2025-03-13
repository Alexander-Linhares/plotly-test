import plotly.graph_objects as go

ages = [19, 18, 23, 18, 17, 24, 20]
scores = [5, 7, 7, 10, 5, 8.5, 7.6]

fig = go.Figure(data = go.Scatter(
    x = ages, 
    y = scores,
    mode = "markers",
    marker = dict(
        color="blue"
    )
))

fig.update_layout(
    title="notas dos alunos por idade",
    xaxis_title="Idades",
    yaxis_title="Pontuação"
)

fig.update_traces(error_y=dict(
    type = "data",
    array = [3, 2, 4, 1, 2 ,3, 4],
    visible = True
))

fig.show()