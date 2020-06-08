"""
The layout file for the Dashboard web page.
Layout file contains the structure of the web page for the dashboard in HTML format.
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import calendar
import datetime as dt
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from database import *
from tab_country import tab1_layout
from tab_world import tab2_layout


page_layout = html.Div(children= [
	
	html.Div(children=[

		html.Div(children=[	

			html.Div(children=[

				html.Center([
					html.H3("COVID-19"),
					html.H3("Dashboard")
				])

			], style= {
				'width':'22%',
				'display':'inline-block',
			}, className= 'four columns'),

			html.Div(children=[

				html.Center([
					html.B(children= [html.H3(format(total_cases_world,','), style={'color':'#FF3333'})]),
					html.H5("Total cases in the world")
				])

			], style= {
				'width':'22%',
				'marginLeft':'8%',
				'display':'inline-block',
				'border':'thin lightgrey solid',
				'box-shadow': '6px 6px 6px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns'),

			html.Div(children=[

				html.Center([
					html.B(children= [html.H3(format(int(total_recovered_world),','), style={'color':'#FF3333'})]),
					html.H5("Total recoveries"),
				])

			], style= {
				'width':'22%',
				'marginLeft':'1%',
				'display':'inline-block',
				'border':'thin lightgrey solid',
				'box-shadow': '6px 6px 6px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns'),

			html.Div(children=[

				html.Center([
					html.B(children= [html.H3(format(total_deaths_world,','), style={'color':'#FF3333'})]),
					html.H5("Total deaths"),
				])

			], style= {
				'width':'22%',
				'display':'inline-block',
				'marginLeft':'1%',
				'border':'thin lightgrey solid',
				'box-shadow': '6px 6px 6px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns')

		], style= {
			'display':'inline-block',
			'width':'100%',
		}, className= 'row')

	], style= {
		'display':'inline-block',
		'width':'100%',
		'textAlign':'right'
	}),

	html.Hr(style={'height':'2px'}),

	dcc.Tabs(

		id= 'tab-select',
		children= [

			dcc.Tab(label= 'Country Statistics', value= 'tab-1'),
			dcc.Tab(label= 'World Statistics', value= 'tab-2')
		]
	),

	html.Br(),

	html.Div(id= 'tab-content')

], style= {'width':'100%','backgroundColor':'white'})