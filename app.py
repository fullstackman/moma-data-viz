# -*- coding: utf-8 -*-

import dash
import pandas as pd

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

print("\tLoading the artwork data set. . .")
artworkSet = pd.read_csv('data/F2.csv', low_memory = False, encoding = 'utf8')
print("\t\tSuccess!")

print("\tLoading the country data set. . .")
countrySet = pd.read_csv('data/nMaps.csv', low_memory = False, encoding = 'utf8')
print("\t\tSuccess!")