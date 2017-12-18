# Custom 404 Page
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app

# The flavor of markdown that needs to be used:
# https://daringfireball.net/projects/markdown/syntax

missingno_layout = html.Div([
    html.H1('Page Not Found'),
    html.Div(id='404-content'),
    html.Br(),
    html.P('Maybe you typed something wrong in the URL?'),
    dcc.Link('Go back to home', href='/')
])
