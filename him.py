
import plotly.graph_objects as go

import dash
from dash import dcc
import dash_bootstrap_components as dbc
fig = go.Figure()
import pandas as pd
import dash
import plotly.express as px
import pandas as pd
from dash import Input, Output, html, dcc


app = dash.Dash(
    __name__,
    assets_external_path='https://www.w3schools.com/w3css/4/w3.css/'
)
title1 = html.H1("Himilo-Solutions", style={'textAlign': 'center'})
title = html.H1("Waayo-Aarag Matchs Statistics", style={'textAlign': 'center'})

Survey = pd.read_csv('Survey.csv')
heads = ['Month', 'Ahmed_S',
         'Ali', 'Salo', 'Baxraawi', 'Idiris', 'Mustafe','Mukhtar','Jiiro','Hamse','M_Hassan','Janaale','Abshir','Cabdiraxman','Ahmed_C']
df = Survey.groupby(heads)['Ahmed_S'].apply(pd.Series.count)

df = pd.DataFrame(df)
df = df.stack()
df = pd.DataFrame(df)
df = df.unstack().reset_index()

df.columns = ['Month',  'Ahmed_S',
              'Ali', 'Salo', 'Baxraawi', 'Idiris', 'Mustafe', 'Mukhtar','Jiiro','Hamse','M_Hassan','Janaale','Abshir','Cabdiraxman','Ahmed_C','Scale']
# input1 = dbc.Col(dcc.Dropdown(id = 'drop1' ,options = [{'label':x,'value':x} for x in df['Tenure'].unique()],value = " 46 to 55"))
input2 = dbc.Col(dcc.Dropdown(id='drop2', options=[{'label': x, 'value': x} for x in df['Month'].unique()],
                             value= 'April'))

output1 = dbc.Col(dcc.Graph(id='myfig1', figure={}))
output2 = dbc.Col(dcc.Graph(id='myfig2', figure={}))
output3 = dbc.Col(dcc.Graph(id='myfig3', figure={}))
output4 = dbc.Col(dcc.Graph(id='myfig4', figure={}))
output5 = dbc.Col(dcc.Graph(id='myfig5', figure={}))
output6 = dbc.Col(dcc.Graph(id='myfig6', figure={}))
output7 = dbc.Col(dcc.Graph(id='myfig7', figure={}))
output8 = dbc.Col(dcc.Graph(id='myfig8', figure={}))
output9 = dbc.Col(dcc.Graph(id='myfig9', figure={}))
output10 = dbc.Col(dcc.Graph(id='myfig10', figure={}))
output11 = dbc.Col(dcc.Graph(id='myfig11', figure={}))
output12 = dbc.Col(dcc.Graph(id='myfig12', figure={}))
output13 = dbc.Col(dcc.Graph(id='myfig13', figure={}))
output14 = dbc.Col(dcc.Graph(id='myfig14', figure={}))


row1 = dbc.Row([input2])
#row2 = dbc.Row([output1, output2, output3])
#row3 = dbc.Row([output4, output5, output6])


app.layout = dbc.Container([title1,title,row1,output1,output2,output3,output4,output5,output6,output7,
                            output8,output9,output10,output11,output12,output13,output14 ])


@app.callback(
    Output(component_id="myfig1", component_property='figure'),
    Output(component_id="myfig2", component_property='figure'),
    Output(component_id="myfig3", component_property='figure'),
    Output(component_id="myfig4", component_property='figure'),
    Output(component_id="myfig5", component_property='figure'),
    Output(component_id="myfig6", component_property='figure'),
    Output(component_id="myfig7", component_property='figure'),
    Output(component_id="myfig8", component_property='figure'),
    Output(component_id="myfig9", component_property='figure'),
    Output(component_id="myfig10", component_property='figure'),
    Output(component_id="myfig11", component_property='figure'),
    Output(component_id="myfig12", component_property='figure'),
    Output(component_id="myfig13", component_property='figure'),
    Output(component_id="myfig14", component_property='figure'),

    Input(component_id='drop2', component_property='value'),

)
def himilo(var1):
    dff = df[(df["Month"] == var1)]

    fig1 = px.pie(dff, names="Ahmed_S", values="Scale", title="1-Ahmed_Suleiman")
    fig2 = px.pie(dff, names="Ali", values="Scale", title="2-Ali ")
    fig3 = px.pie(dff, names="Salo", values="Scale", title="3-Salo ")

    fig4 = px.pie(dff, names="Baxraawi", values="Scale", title="4-Baxraawi ")
    fig5 = px.pie(dff, names="Idiris", values="Scale", title="5-Idiris  ")
    fig6 = px.pie(dff, names="Mustafe", values="Scale", title="6-Mustafe ")

    fig7 = px.pie(dff, names="Mukhtar", values="Scale", title="7-Mukhtar ")
    fig8 = px.pie(dff, names="Jiiro", values="Scale", title="8-Jiiro")

    fig9 = px.pie(dff, names="Hamse", values="Scale", title="9-Hamse ")
    fig10 = px.pie(dff, names="M_Hassan", values="Scale", title="10-M_Hassan")

    fig11 = px.pie(dff, names="Janaale", values="Scale", title="11-Janaale ")
    fig12 = px.pie(dff, names="Abshir", values="Scale", title="12-Abshir ")
    fig13 = px.pie(dff, names="Cabdiraxman", values="Scale", title="13-Cabdiraxman ")
    fig14 = px.pie(dff, names="Ahmed_C", values="Scale", title="14-Ahmed_Cabdilaahi ")

    return fig1, fig2, fig3, fig4, fig5, fig6,fig7,fig8,fig9,fig10,fig11, fig12, fig13, fig14



app.run(host='0.0.0.0' port=5000)
server = app.server
