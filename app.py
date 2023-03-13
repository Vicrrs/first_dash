import dash
from dash import html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")

# Trabalhando com layout
app.layout = html.Div(id="div1",
                      children=[
                          html.H1("First Dash", id="div1"),

                          html.Div("Dash: Um framework web para Python"),

                          dcc.Graph(figure=fig, id="graph")
                      ]
                      )

if __name__ == "__main__":
    app.run_server(debug=True)
