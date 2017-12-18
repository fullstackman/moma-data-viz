# The heatmap page
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app, artworkSet, countrySet

import pandas as pd
import numpy as np
import io

print("Getting the heatmap ready:")
country = countrySet
country = country.rename(index=str, columns={"nationality": "Nationality_y"})
finalArt = pd.merge(country,artworkSet,how = 'left',on = 'Nationality_y')
Art_pivot = pd.pivot_table(finalArt,index = 'alpha_3_code', aggfunc = 'count')
alpha_pivot = Art_pivot.to_records()

df = pd.DataFrame(alpha_pivot)
dff = pd.merge(df,country,how = 'left',on = 'alpha_3_code')
dff = pd.merge(df,country,how = 'left',on = 'alpha_3_code')
dff['logCount'] = 0
for i in range(0,len(dff['Artist']),1):
    if dff.loc[i,'Artist'] == 0:
        pass
    else:
        dff.loc[i,'logCount'] = np.log(dff.loc[i,'Artist'])

df['text'] = dff['en_short_name_y'].astype(str) + '<br>' +    'Number of ArtWorks: '+dff['Artist'].astype(str)
print("\tSuccess!")
print("Creating the heat map. . .")
sampleData = [ dict(
        type = 'choropleth',
        locations = dff['alpha_3_code'],
        z = dff['logCount'],
        text = df[ 'text'],
        colorscale = [
        [0,"rgb(220, 220, 220)"],
        [0.35,"rgb(255, 249, 89)"],
        [0.5,"rgb(255, 211, 89)"],
        [0.6,"rgb(255, 187, 0)"],
        [0.7,"rgb(255, 81, 0)"],
        [1,"rgb(255, 0, 0)"]
        ],
        #colorscale = [[0,"rgb(255, 10, 5)"],[0.35,"rgb(190, 60, 40)"],[0.5,"rgb(245, 100, 70)"],[0.6,"rgb(245, 120, 90)"],[0.7,"rgb(190, 60, 40)"],[1,"rgb(245, 100, 70)"]],
        autocolorscale = False,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = 'Concentration of Artwork'),
      ) ]

sampleLayout = dict(
    title = 'MoMA Artworks by Country',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

# please change this variable name
page_1_layout = html.Div([
    html.Div(id='heatmap-content'),
    html.H1('Heatmap of Artworks by country of origin'),
    dcc.Markdown(children="Here is our heatmap:"),
    dcc.Graph(
        id='heatmap1',
        figure={
            'data': sampleData,
            'layout': sampleLayout
        }
    )
])


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])

def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)