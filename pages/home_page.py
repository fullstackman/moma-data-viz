# The Home Page
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app

dummyIntro='''## Purpose
Art museums generally have websites that showcase the artwork in their collection, but sometimes it can be difficult to:
*   Figure out if the collection of art is representative of different countries and which countries contribute the greatest number of artworks
*   Determine how the collection of art has changed over time
*   See how a piece of art compares to other artwork in the collection
The Museum of Modern Art (MoMA) is an example of a popular art museum where the website lacks these useful functionalities. Our website, The MoMA and More, uses visualizations and a searchable tool to enable website visitors to explore information on the collection of art at the MoMA and how that collection has changed over time.

Specifically, our website involves three primary components:
1.  Interactive heatmap of the number of artworks acquired from countries around the world
2.  Interactive timeline of the number of artworks in each department acquired each year
3.  Searchable tool that allows the user to compare a piece of artwork to the rest of the MoMA collection
'''

index_page = html.Div([
    html.Div([
        html.Div([
            html.H1('The MOMA and More!', style={
                'padding': '20vh 0 0 0'
            }),
            html.P("Built using Dash (a web application framework for data visualization in Python).")
        ], style={
            'color': 'white',
            'textAlign': 'center',
            'textShadow': '1px -1px 14px black'
        })
    ], style={
        'background': 'url(https://images.unsplash.com/photo-1469510038946-6bf892bbe9d6?auto=format&fit=crop&w=1050&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D)',
        'background-repeat': 'no-repeat',
        'width': '100%',
        'min-height': '85vh'
    }),
    dcc.Markdown(children=dummyIntro)
])
