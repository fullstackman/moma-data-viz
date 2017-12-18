print("\tImporting dependencies. . .")
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app
from pages import navbar, home_page, custom404_page, search_page, heatmap_page, timeline_page

print("\tSetting up app directory. . .")
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar.navigation_bar,
    html.Div(id='page-content')
], id='mainAppLayout')

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page.index_page
    elif pathname == '/heatmap':
        return heatmap_page.page_1_layout
    elif pathname == '/timeline':
        return timeline_page.page_2_layout
    elif pathname == '/search':
        return search_page.search_layout
    else:
	    # Our 404 "URL not found" page
        return custom404_page.missingno_layout

app.css.append_css({
    'external_url': 'https://codepen.io/fullstackman/pen/ypYMwR.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)