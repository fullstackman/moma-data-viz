# The Timeline Page
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app, artworkSet

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import io
import numpy as np

print("Getting the timeline ready:")
df = artworkSet
df[['Ayear', 'Amonth', 'Aday']] = df['DateAcquired'].str.split('-', expand=True)
#df['nDate'].describe()
ref = pd.pivot_table(df, index = 'Department', aggfunc = 'count')
ref = ref.to_records()
ref = pd.DataFrame(ref)
slist = list(ref['Department'])

print("Running counts on the different departments. . .")
data_2004 = df[df['Department'] == slist[0]]
print("\tArcD")
ArcD = df[df['Department'] == slist[1]]
ArcD = pd.pivot_table(ArcD,index = 'Ayear', aggfunc = 'count')
ArcD = ArcD.to_records()
ArcD = pd.DataFrame(ArcD)
if(not ArcD.empty):
    ArcD = ArcD[['Ayear','ConstituentID_x']]
    ArcD = ArcD.rename(index = str, columns = {'ConstituentID_x':'ArcDCo'})
else:
    print("\tThat data frame was empty!")
print("\tDrw")
Drw = df[df['Department'] == slist[3]]
Drw = pd.pivot_table(Drw,index = 'Ayear',aggfunc = 'count')
Drw = Drw.to_records()
Drw = pd.DataFrame(Drw)
if(not Drw.empty):
    Drw = Drw[['Ayear','ConstituentID_x']]
    Drw = Drw.rename(index = str, columns = {'ConstituentID_x':'DrwCo'})
else:
    print("\tThat data frame was empty!")
print("\tFlm")
Flm = df[df['Department'] == slist[4]]
Flm = pd.pivot_table(Flm,index = 'Ayear',aggfunc = 'count')
Flm = Flm.to_records()
Flm = pd.DataFrame(Flm)
if(not Flm.empty):
    Flm = Flm[['Ayear','ConstituentID_x']]
    Flm = Flm.rename(index = str, columns = {'ConstituentID_x':'FlmCo'})
else:
    print("\tThat data frame was empty!")
print("\tFlx")
Flx = df[df['Department'] == slist[5]]
Flx = pd.pivot_table(Flx,index = 'Ayear',aggfunc = 'count')
Flx = Flx.to_records()
Flx = pd.DataFrame(Flx)
if(not Flx.empty):
    Flx = Flx[['Ayear','ConstituentID_x']]
    Flx = Flx.rename(index = str, columns = {'ConstituentID_x':'FlxCo'})
else:
    print("\tThat data frame was empty!")
print("\tMP")
MP = df[df['Department'] == slist[6]]
MP = pd.pivot_table(MP,index = 'Ayear',aggfunc = 'count')
MP = MP.to_records()
MP = pd.DataFrame(MP)
if(not MP.empty):
    MP = MP[['Ayear','ConstituentID_x']]
    MP = MP.rename(index = str, columns = {'ConstituentID_x':'MPCo'})
else:
    print("\tThat data frame was empty!")
print("\tPS")
PS = df[df['Department'] == slist[7]]
PS = pd.pivot_table(PS,index = 'Ayear',aggfunc = 'count')
PS = PS.to_records()
PS = pd.DataFrame(PS)
if(not PS.empty):
    PS = PS[['Ayear','ConstituentID_x']]
    PS = PS.rename(index = str, columns = {'ConstituentID_x':'PSCo'})
else:
    print("\tThat data frame was empty!")
print("\tPtg")
Ptg = df[df['Department'] == slist[2]]
Ptg = pd.pivot_table(Ptg,index = 'Ayear',aggfunc = 'count')
Ptg = Ptg.to_records()
Ptg = pd.DataFrame(Ptg)
if(not Ptg.empty):
    Ptg = Ptg[['Ayear','ConstituentID_x']]
    Ptg = Ptg.rename(index = str, columns = {'ConstituentID_x':'PtgCo'})
else:
    print("\tThat data frame was empty!")
print("\tPI")
PI = df[df['Department'] == slist[8]]
PI = pd.pivot_table(PI,index = 'Ayear',aggfunc = 'count')
PI = PI.to_records()
PI = pd.DataFrame(PI)
if(not PI.empty):
    PI = PI[['Ayear','ConstituentID_x']]
    PI = PI.rename(index = str, columns = {'ConstituentID_x':'PICo'})
else:
    print("\tThat data frame was empty!")
print("Done! Now let's put it all together. . .")
clump = pd.merge(ArcD,Drw, how = 'left', on = 'Ayear')
clump = pd.merge(clump,Flm, how = 'left', on = 'Ayear')
clump = pd.merge(clump,Flx, how = 'left', on = 'Ayear')
clump = pd.merge(clump,MP, how = 'left', on = 'Ayear')
clump = pd.merge(clump,Ptg, how = 'left', on = 'Ayear')
clump = pd.merge(clump,PI, how = 'left', on = 'Ayear')
clump = pd.merge(clump,PS, how = 'left', on = 'Ayear')

print("Drawing the plot. . .")
trace1 = go.Scatter(
    x=ArcD['Ayear'],
    y=ArcD['ArcDCo'],
    name='ArcD',
    mode = 'lines'
)
trace2 = go.Scatter(
    x=Drw['Ayear'],
    y=Drw['DrwCo'],
    name='Drw',
    mode = 'lines'
)
trace3 = go.Scatter(
    x=Flm['Ayear'],
    y=Flm['FlmCo'],
    name='flm',
    mode = 'lines'
)
trace4 = go.Scatter(
    x=Flx['Ayear'],
    y=Flx['FlxCo'],
    name='FLX',
    mode = 'lines'
)
trace5 = go.Scatter(
    x=MP['Ayear'],
    y=MP['MPCo'],
    name='MeP',
    mode = 'lines'
)
trace7 = go.Scatter(
    x=PI['Ayear'],
    y=PI['PICo'],
    name='Print',
    mode = 'lines'
)
trace8 = go.Scatter(
    x=PS['Ayear'],
    y=PS['PSCo'],
    name='Paint Sculp',
    mode = 'lines'
)

finalData = [trace1, trace2,trace3,trace4,trace5,trace7,trace8]
finalLayout = go.Layout(
    barmode='stack',
    autosize=False,
    width=900,
    height=900,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
)

# please change this variable name
page_2_layout = html.Div([
    html.H1('Timeline of Acquired Works'),
    dcc.Graph(
        id='timeline1',
        figure={
            'data': finalData,
            'layout': finalLayout
        }
    ),
    html.Div(id='timeline-content'),
    html.Br()
])

@app.callback(dash.dependencies.Output('timeline-content', 'children'),
              [dash.dependencies.Input('timeline-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)
