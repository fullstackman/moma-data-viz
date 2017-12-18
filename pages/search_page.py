# The search page
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from app import app, artworkSet, countrySet
from utilities import nation, dep
from searchLibrary import runSearch

search_layout = html.Div([
	html.H1('Custom Search'),
	html.P('Use the filters below to search for some of the most popular artists in the museum\'s collection.'),
	html.Div([
		html.H3('Artist Nationality'),
	    dcc.Dropdown(
	    	id='nation_selector',
		    # iterate the nation list of SNY.py to generate the options
		    options=[
		        {'label': nationality, 'value': nationality} for nationality in nation
		    ]
		),
		html.H3('MoMA Department'),
	    dcc.Dropdown(
	    	id='department_selector',
		    # iterate the nation list of SNY.py to generate the options
		    options=[
		        {'label': department, 'value': department} for department in dep
		    ]
		),
		html.H3('Time Period'),
		dcc.RangeSlider(
			id='date_selector',
		    count=1,
		    min=1933,
		    max=2017,
		    step=1,
		    value=[1945, 2001]
		),
		html.P(id='date_range'),
	    html.Button(id='submit-button', n_clicks=0, children='Submit')
	], style={
		'width': '55%',
		'display': 'inline-block',
		'margin': '0 15px'
	}),
	html.Div([
		html.H2('Output'),
	    html.P(id='resultsArea')
	], style={
    	'width': '35%',
    	'display': 'inline-block',
    	'vertical-align': 'top',
    	'margin': '0 15px'
	})
])

@app.callback(Output('date_range', 'children'),
              [Input('date_selector', 'value')])
def showDates(givenRange):
    return u'''
        The selected dates are {} to {}
    '''.format(givenRange[0],givenRange[1])

@app.callback(Output('resultsArea', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('nation_selector', 'value'),
               State('department_selector', 'value'),
               State('date_selector', 'value')])
def update_output(n_clicks, givenNation, givenDepartment, givenDates):
	# perform the search
	if(n_clicks > 0):
		searchOutput = runSearch(givenNation,givenDepartment,givenDates[0],givenDates[1])
		return 'Search #{} returned:\n{}\n{}\n{}'.format(n_clicks,searchOutput[0],searchOutput[1],searchOutput[2])
	return 'Nothing to display.'