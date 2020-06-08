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

tab2_layout= html.Div(children= [

	html.Center(children= [

		html.Div(children= [
			dcc.Graph(
				id= 'spread-map',
				style={
					'width':'100%'
				},
				figure= go.Figure(
					data= [
						go.Choropleth(
							locations= overall_df.country,
							locationmode= 'country names',
							z= np.log10(overall_df.total_cases),
							colorscale= 'RdBu',
							autocolorscale= False,
							text= overall_df.total_cases,
							hovertemplate= '%{location}: %{text:.0f}<extra></extra>',
							reversescale= True,
							marker_line_color= 'darkgrey',
							marker_line_width= 0.1,
							showscale= False
						)
					],

					layout= go.Layout(
						title= {'text':'<b>Spread of COVID-19 throughout the World</b>', 'x':0.5, 'y':0.95},
						geo= dict(
							showframe= False,
							showcoastlines= False,
							projection_type= 'equirectangular'
						),
						height=400,
						plot_bgcolor= '#F8F8F8',
						margin= dict(l=5,t=13,b=0,r=5)
					)
				)
			)

		], style={
			'width':'50%',
			'border':'thin lightgrey solid',
			'box-shadow': '6px 6px 6px lightgrey',
		})
	])
])