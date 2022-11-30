
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


app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
title = html.H1("Strategic Planning Presentationss", style={'textAlign': 'center'})

Survey = pd.read_excel('Survey.xlsx')
heads = ['Position', 'Tenure', 'Adaptability',
         'No_pressure', 'Awareness', 'Likelihood', 'Influence', 'Importance',
         'DefinedGoals', 'ReachGoal', 'Rewards', 'ParticiptionGoals',
         'Improvement', 'HarmonyGoals', 'CustomerValue', 'PolicyLeads',
         'CustomerRetension', 'CustomerExperience', 'ExcellentReward',
         'Satisfaction', 'Competency', 'TeamWork', 'TechnicalSkills',
         'clearRoles', 'Collaboration', 'Crossfunctional', 'RespectUniqueness',
         'PriorityObjectives', 'ProctedPolicies', 'FactDrivenDecisions',
         'AvailableInfo', 'CoreValue', 'CommunicationDepartment',
         'CommunicationEmployee', 'CommunicationManagers', 'Encourage',
         'FreedomExpress', 'DepartmentValues']
df = Survey.groupby(heads)['Adaptability'].apply(pd.Series.count)

df = pd.DataFrame(df)
df = df.stack()
df = pd.DataFrame(df)
df = df.unstack().reset_index()

df.columns = ['Position', 'Tenure', 'Adaptability',
              'No_pressure', 'Awareness', 'Likelihood', 'Influence', 'Importance',
              'DefinedGoals', 'ReachGoal', 'Rewards', 'ParticiptionGoals',
              'Improvement', 'HarmonyGoals', 'CustomerValue', 'PolicyLeads',
              'CustomerRetension', 'CustomerExperience', 'ExcellentReward',
              'Satisfaction', 'Competency', 'TeamWork', 'TechnicalSkills',
              'clearRoles', 'Collaboration', 'Crossfunctional', 'RespectUniqueness',
              'PriorityObjectives', 'ProctedPolicies', 'FactDrivenDecisions',
              'AvailableInfo', 'CoreValue', 'CommunicationDepartment',
              'CommunicationEmployee', 'CommunicationManagers', 'Encourage',
              'FreedomExpress', 'DepartmentValues', 'Scale']
# input1 = dbc.Col(dcc.Dropdown(id = 'drop1' ,options = [{'label':x,'value':x} for x in df['Tenure'].unique()],value = " 46 to 55"))
input2 = dbc.Col(dcc.Dropdown(id='drop2', options=[{'label': x, 'value': x} for x in df['Position'].unique()],
                              value="Department Manager"))

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
output15 = dbc.Col(dcc.Graph(id='myfig15', figure={}))
output16 = dbc.Col(dcc.Graph(id='myfig16', figure={}))
output17 = dbc.Col(dcc.Graph(id='myfig17', figure={}))
output18 = dbc.Col(dcc.Graph(id='myfig18', figure={}))
output19 = dbc.Col(dcc.Graph(id='myfig19', figure={}))
output20 = dbc.Col(dcc.Graph(id='myfig20', figure={}))
output21 = dbc.Col(dcc.Graph(id='myfig21', figure={}))

output22 = dbc.Col(dcc.Graph(id='myfig22', figure={}))
output23 = dbc.Col(dcc.Graph(id='myfig23', figure={}))
output24 = dbc.Col(dcc.Graph(id='myfig24', figure={}))
output25 = dbc.Col(dcc.Graph(id='myfig25', figure={}))
output26 = dbc.Col(dcc.Graph(id='myfig26', figure={}))
output27 = dbc.Col(dcc.Graph(id='myfig27', figure={}))

output28 = dbc.Col(dcc.Graph(id='myfig28', figure={}))
output29 = dbc.Col(dcc.Graph(id='myfig29', figure={}))
output30 = dbc.Col(dcc.Graph(id='myfig30', figure={}))
output31 = dbc.Col(dcc.Graph(id='myfig31', figure={}))
output32 = dbc.Col(dcc.Graph(id='myfig32', figure={}))
output33 = dbc.Col(dcc.Graph(id='myfig33', figure={}))
output34 = dbc.Col(dcc.Graph(id='myfig34', figure={}))
output35 = dbc.Col(dcc.Graph(id='myfig35', figure={}))
output36 = dbc.Col(dcc.Graph(id='myfig36', figure={}))

row1 = dbc.Row([input2])
row2 = dbc.Row([output1, output2, output3])
row3 = dbc.Row([output4, output5, output6])
row4 = dbc.Row([output7, output8, output9])
row5 = dbc.Row([output10, output11, output12])
row6 = dbc.Row([output13, output14, output15])
row7 = dbc.Row([output16, output17, output18])
row8 = dbc.Row([output19, output20, output21])
row9 = dbc.Row([output22, output23, output24])
row10 = dbc.Row([output25, output26, output27])
row11 = dbc.Row([output28, output29, output30])
row12 = dbc.Row([output31, output32, output33])
row13 = dbc.Row([output34, output35, output36])

app.layout = dbc.Container([title, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13])


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
    Output(component_id="myfig15", component_property='figure'),
    Output(component_id="myfig16", component_property='figure'),
    Output(component_id="myfig17", component_property='figure'),
    Output(component_id="myfig18", component_property='figure'),
    Output(component_id="myfig19", component_property='figure'),
    Output(component_id="myfig20", component_property='figure'),
    Output(component_id="myfig21", component_property='figure'),
    Output(component_id="myfig22", component_property='figure'),
    Output(component_id="myfig23", component_property='figure'),
    Output(component_id="myfig24", component_property='figure'),
    Output(component_id="myfig25", component_property='figure'),
    Output(component_id="myfig26", component_property='figure'),
    Output(component_id="myfig27", component_property='figure'),
    Output(component_id="myfig28", component_property='figure'),
    Output(component_id="myfig29", component_property='figure'),
    Output(component_id="myfig30", component_property='figure'),
    Output(component_id="myfig31", component_property='figure'),
    Output(component_id="myfig32", component_property='figure'),
    Output(component_id="myfig33", component_property='figure'),
    Output(component_id="myfig34", component_property='figure'),
    Output(component_id="myfig35", component_property='figure'),
    Output(component_id="myfig36", component_property='figure'),

    Input(component_id='drop2', component_property='value'),

)
def himilo(var1):
    dff = df[(df["Position"] == var1)]

    fig1 = px.pie(dff, names="Adaptability", values="Scale", title="1-Adaptability ")
    fig2 = px.pie(dff, names="No_pressure", values="Scale", title="2-No_pressure ")
    fig3 = px.pie(dff, names="Awareness", values="Scale", title="3-Awareness ")

    fig4 = px.pie(dff, names="Likelihood", values="Scale", title="4-Likelihood ")
    fig5 = px.pie(dff, names="Influence", values="Scale", title="5-Influence  ")
    fig6 = px.pie(dff, names="Importance", values="Scale", title="6-Importance ")

    fig7 = px.pie(dff, names="DefinedGoals", values="Scale", title="7-DefinedGoals ")
    fig8 = px.pie(dff, names="ReachGoal", values="Scale", title="8-ReachGoal  ")
    fig9 = px.pie(dff, names="Rewards", values="Scale", title="9-Rewards ")

    fig10 = px.pie(dff, names="ParticiptionGoals", values="Scale", title="10-ParticiptionGoals ")
    fig11 = px.pie(dff, names="Improvement", values="Scale", title="11-Improvement ")
    fig12 = px.pie(dff, names="HarmonyGoals", values="Scale", title="12-HarmonyGoals ")

    fig13 = px.pie(dff, names="CustomerValue", values="Scale", title="13-CustomerValue ")
    fig14 = px.pie(dff, names="ExcellentReward", values="Scale", title="14-ExcellentReward ")
    fig15 = px.pie(dff, names="PolicyLeads", values="Scale", title="15-PolicyLeads Percentage ")

    fig16 = px.pie(dff, names="CustomerRetension", values="Scale", title="16-CustomerRetension ")
    fig17 = px.pie(dff, names="CustomerExperience", values="Scale", title="17-CustomerExperience ")
    fig18 = px.pie(dff, names="Satisfaction", values="Scale", title="18-Satisfaction  ")

    fig19 = px.pie(dff, names="Competency", values="Scale", title="19-Competency ")
    fig20 = px.pie(dff, names="TeamWork", values="Scale", title="20-TeamWork ")
    fig21 = px.pie(dff, names="TechnicalSkills", values="Scale", title="21-TechnicalSkills  ")

    fig22 = px.pie(dff, names="clearRoles", values="Scale", title="22-clearRoles ")
    fig23 = px.pie(dff, names="Collaboration", values="Scale", title="23-Collaboration ")
    fig24 = px.pie(dff, names="Crossfunctional", values="Scale", title="24-Crossfunctional ")

    fig25 = px.pie(dff, names="RespectUniqueness", values="Scale", title="25-RespectUniqueness  ")
    fig26 = px.pie(dff, names="PriorityObjectives", values="Scale", title="26-PriorityObjectives ")
    fig27 = px.pie(dff, names="ProctedPolicies", values="Scale", title="27-ProctedPolicies ")

    fig28 = px.pie(dff, names="FactDrivenDecisions", values="Scale", title="28-FactDrivenDecisions ")
    fig29 = px.pie(dff, names="AvailableInfo", values="Scale", title="29-AvailableInfo ")
    fig30 = px.pie(dff, names="CoreValue", values="Scale", title="30-CoreValue  ")

    fig31 = px.pie(dff, names="CommunicationDepartment", values="Scale", title="31-CommunicationDepartment ")
    fig32 = px.pie(dff, names="CommunicationEmployee", values="Scale", title="32-CommunicationEmployee ")
    fig33 = px.pie(dff, names="CommunicationManagers", values="Scale", title="33-CommunicationManagers ")

    fig34 = px.pie(dff, names="Encourage", values="Scale", title="34-Encourage  ")
    fig35 = px.pie(dff, names="FreedomExpress", values="Scale", title="35-FreedomExpress ")
    fig36 = px.pie(dff, names="DepartmentValues", values="Scale", title="36-DepartmentValues ")

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13, fig14, fig15, fig16, fig17, fig18, fig19, fig20, fig21, fig22, fig23, fig24, fig25, fig26, fig27, fig28, fig29, fig30, fig31, fig32, fig33, fig34, fig35, fig36

app.run_server(debug=True, port=80)
server = app.server
