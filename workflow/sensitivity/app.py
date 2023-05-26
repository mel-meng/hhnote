from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = px.data.stocks()


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Sensitivity Analysis', style={'textAlign':'center'}),
    html.P('Adjust the parameter sliders to see the calibration Results, adjust the parameters value from -50% to 50%'),
    # dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    
    html.Div(children=[
        html.Div(children=[
            html.P("Param 1:"),
            dcc.Slider(min=-50, max=50, step=25, value=0, id='p1-slider', vertical=True, verticalHeight=100)

        ],
        style={'display': 'inline-block'}
        ), 
        html.Div(children=[
            html.P("Param 2:"),
            dcc.Slider(min=-50, max=50, step=25, value=0, id='p2-slider', vertical=True, verticalHeight=100),

        ],
        style={'display': 'inline-block'}
        )
    ]),
    

    
    
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('p1-slider', 'value'),
    Input('p2-slider', 'value')
)
def update_graph(p1, p2):
    print(p1)
    print(p2)
    df0 = df.copy()
    df0['OBS'] = df0['GOOG']
    df0['CAL'] = df0['GOOG']*(p1+100)/100 + 0.3*(100+p2)/100
    fig = px.line(df0, x="date", y=['OBS', 'CAL'],#df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='Sim vs Obs')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)