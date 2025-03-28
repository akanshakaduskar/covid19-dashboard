#importing all the dependencies
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import dash
# import dash_html_components as html
from dash import dcc
from dash.dependencies import Input,Output
import plotly.express as px
from dash import html
plotly.graph_objs.scatter.Line
plotly.graph_objs.layout.shape.Line

external_stylesheet = [
    {
         'href':"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
         'rel':"stylesheet",
         'integrity':"sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
         'crossorigin':"anonymous"
    }
]

#to read csv file
patients = pd.read_csv('state_wise_daily.csv')

#here we are using masking to know the status of each column
total = patients.shape[0]
active = patients[patients['Status'] == 'Confirmed'].shape[0]
recovered = patients[patients['Status'] == 'Recovered'].shape[0]
death = patients[patients['Status'] == 'Deceased'].shape[0]

#here we are giving list for dropdown
options=[
    {'label' : 'All','value':'All'},
    {'label' : 'Hospitalized','value':'Hospitalized'},
    {'label' : 'Recovered','value':'Recovered'},
    {'label' : 'Deceased','value':'Deceased'}
]

options1 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}
]

options2 = [

    {'label': 'Red Zone', 'value': 'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'}
]

#LOCAL HOST
app = dash.Dash(__name__,external_stylesheets=external_stylesheet)

#Layout
app.layout = html.Div([
    html.H1('Corona Virus Pandemic',style={'color' :'#fff','text-align' : 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Total Cases", className='text-light'),
                        html.H4(total,className='text-light')
                    ])
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Active Cases", className='text-light'),
                        html.H4(active, className='text-light')
                    ])
                ], className='card-body')
            ], className='card bg-info')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Recovered Cases", className='text-light'),
                        html.H4(recovered, className='text-light')
                    ])
                ], className='card-body')
            ], className='card bg-warning')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Total Deaths", className='text-light'),
                        html.H4(death, className='text-light')
                    ])
                ], className='card-body')
            ], className='card bg-success')
        ],className='col-md-3')
    ],className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph', options=options1, value='All'),
                    dcc.Graph(id='graph')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=options2, value='Status', style={"width": "100%"}),
                    dcc.Graph(id='the_graph')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-6')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    #for graph we used core component of dash i.e dcc
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ],className='row')
],className='Container')

#here we are using decorater function i.e @app.callback
@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])

def update_graph(type):
    if type == 'All':
        return {'data': [go.Bar(x=patients['State'], y=patients['Total'])],
                'layout': go.Layout(title="State Total Count", plot_bgcolor='orange')}
    if type == "Hospitalized":
        return {'data': [go.Bar(x=patients['State'], y=patients['Hospitalized'])],
                'layout': go.Layout(title="State Total Count", plot_bgcolor='orange')}
    if type == "Recovered":
        return {'data': [go.Bar(x=patients['State'], y=patients['Recovered'])],
                'layout': go.Layout(title="State Total Count", plot_bgcolor='orange')}
    if type == "Deceased":
        return {'data': [go.Bar(x=patients['State'], y=patients['Deceased'])],
                'layout': go.Layout(title="State Total Count", plot_bgcolor='orange')}


@app.callback(Output('graph', 'figure'), [Input('plot-graph', 'value')])
def generate_graph(type):
    if type == 'All':
        return {'data': [go.Line(x=patients['Status'], y=patients['Total'])],
                'layout': go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}
    if type == 'Mask':
        return {'data': [go.Line(x=patients['Status'], y=patients['Mask'])],
                'layout': go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}
    if type == 'Sanitizer':
        return {'data': [go.Line(x=patients['Status'], y=patients['Sanitizer'])],
                'layout': go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}
    if type == 'Oxygen':
        return {'data': [go.Line(x=patients['Status'], y=patients['Oxygen'])],
                'layout': go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}

@app.callback(Output('the_graph', 'figure'), [Input('my_dropdown', 'value')])
def generate_graph(my_dropdown):
    pie_chart = px.pie(data_frame=patients, names=my_dropdown, hole=0.3)
    return pie_chart

#FLASK LOCAL HOST
if __name__ == '__main__':
    app.run_server(debug = True)

