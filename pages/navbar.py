# The navigation bar that will be present on all pages
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app

# The more complicated styling is hidden in this style sheet:
# https://codepen.io/fullstackman/pen/ypYMwR.css
navigation_bar = html.Nav([
	html.Div([
		html.Img(src='https://placehold.it/50x50')
	]),
	html.Div([
		dcc.Link('Home', href='/'),
		dcc.Link('Heatmap', href='/heatmap'),
		dcc.Link('Timeline', href='/timeline'),
		dcc.Link('Search', href='/search')
		], style={
			'float': 'right',
			'textAlign': 'right'
		})
], style={
	'background': 'purple'
})