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
				'box-shadow': '2px 2px 2px lightgrey',
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
				'box-shadow': '2px 2px 2px lightgrey',
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
				'box-shadow': '2px 2px 2px lightgrey',
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

	html.Div(children=[	

		html.Div(children= [

			html.Div(children= [	

				html.Div(children= [

					html.Div(children= [

						dcc.Graph(
							id= 'daily-case-bullet'
						)

					], style= {
					'width':'48%',
					'border':'thin lightgrey solid',
					'box-shadow': '2px 2px 2px lightgrey',
					'background-color': 'rgb(250, 250, 250)'
					}, className= 'two columns'),

					html.Div(children= [

						dcc.Graph(
							id= 'death-bullet'
						)

					], style= {
					'width':'48%',
					'border':'thin lightgrey solid',
					'box-shadow': '2px 2px 2px lightgrey',
					'background-color': 'rgb(250, 250, 250)'
					}, className= 'two columns')
				], style= {'width':'100%'}, className= 'row'),

				html.Div(children= [

					html.Div(children= [

						dcc.Graph(
							id= 'positive-rate'
						)

					], style= {
					'width':'48%',
					'border':'thin lightgrey solid',
					'box-shadow': '2px 2px 2px lightgrey',
					'background-color': 'rgb(250, 250, 250)'
					}, className= 'two columns'),

					html.Div(children= [

						dcc.Graph(
							id= 'death-rate'
						)

					], style= {
					'width':'48%',
					'border':'thin lightgrey solid',
					'box-shadow': '2px 2px 2px lightgrey',
					'background-color': 'rgb(250, 250, 250)'
					}, className= 'two columns')

				], style= {'marginTop':'1.5%'},
				 className= 'row')

			],style={
				'width':'29%',
				'marginLeft':'2%',
				'display':'inline-block',
			}, className= 'four columns'),


			html.Div(children= [

				dcc.Graph(
					id= 'pie-active-cases'
				)

			], style= {
				'width':'19%',
				'display':'inline-block',
				'marginLeft':'5%',
				'border':'thin lightgrey solid',
				'box-shadow': '2px 2px 2px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns'),

			html.Div(children= [

				dcc.Graph(
					id= 'pie-recovered-cases'
				)

			], style= {
				'width':'19%',
				'display':'inline-block',
				'marginLeft':'2%',
				'border':'thin lightgrey solid',
				'box-shadow': '2px 2px 2px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns'),

			html.Div(children= [

				dcc.Graph(
					id= 'pie-death-cases'
				)

			], style= {
				'width':'19%',
				'display':'inline-block',
				'marginLeft':'2%',
				'border':'thin lightgrey solid',
				'box-shadow': '2px 2px 2px lightgrey',
				'background-color': 'rgb(250, 250, 250)',
			}, className= 'four columns'),

		], style= {
			'height':'30%'
		}, className= 'row'),

		html.Br(),

		html.Div(children= [

			html.Div(children= [

				html.Label(children= [html.B(html.H4('Country'))], style={'marginLeft':'2%'}),

				dcc.RadioItems(
					id= 'country-name',
					options=[{'label':i.capitalize(),'value':i} for i in countries],
					value= 'us'
				),

				html.Br(),

				html.Label(children= [html.B(html.H4('Scale'))], style={'marginLeft':'2%'}),

				dcc.RadioItems(
					id= 'scale-type',
					options= [{'label':i, 'value':i} for i in ['Linear', 'Log']],
					value= 'Linear',
				),

			], style={
			'display':'inline-block',
			'width':'18%',
			'border':'thin lightgrey solid',
			'box-shadow': '2px 2px 2px lightgrey',
			'background-color': 'rgb(250, 250, 250)',
			}, className= 'two columns'),

			html.Div(children= [

				html.Div(children= [

					html.Div(children= [

						html.Div([

							dcc.Graph(
								id= 'line-total-cases',
								style= {'height':'55vh'}
							)

							],
							style={'border':'thin lightgrey solid',
							 'right':'10',
							 'border':'thin lightgrey solid',
							'box-shadow': '2px 2px 2px lightgrey',
							'background-color': 'rgb(250, 250, 250)'
							}),

						html.Br(),

						html.Div([

							dcc.Graph(
								id= 'line-total-deaths',
								style= {'height':'55vh'}
							)

							],
							style={
							'border':'thin lightgrey solid',
							'box-shadow': '2px 2px 2px lightgrey',
							'background-color': 'rgb(250, 250, 250)',
							})
					],
					style= {
						'width':'49%',
						'display':'inline-block',
						'padding':'0 0 0 0'
						},
					className= 'two columns'
					),

					html.Div(children= [

						html.Div(children= [

							dcc.Graph(
								id= 'bar-daily-cases',
								style= {'height':'55vh'}
							)

						],
						style= {
							'border':'thin lightgrey solid',
							'box-shadow': '2px 2px 2px lightgrey',
							'background-color': 'rgb(250, 250, 250)',
							'height':'40%'
						}),

						html.Br(),

						html.Div(children= [

							dcc.Graph(
								id= 'bar-daily-deaths',
								style= {'height':'55vh'}
							)

						],
						style= {
							'border':'thin lightgrey solid',
							'box-shadow': '2px 2px 2px lightgrey',
							'background-color': 'rgb(250, 250, 250)',
							'height':'40%'
						})

					],
					style= {
						'width':'49%',
						'display':'inline-block',
						'padding':'0 0 0 0',
						'marginLeft':'2%'
						},className= 'two columns'
					)

				], style= {'width':'100%'},
				className= 'row'
				)

			], style= {'width':'80%', 'marginLeft':'2%'},
			 className= 'two columns')

		],
		style= {'width':'100%'},
		className= 'row'
		),

		html.Br(),

		html.Div(children= [

			html.Center(children= [

				html.Div(children= [

					html.Label(children= 'Month'),

					dcc.Slider(
						id= 'date-slider',
						min= df.month.min(),
						max= df.month.max(),
						value= df.month.max(),
						marks= {str(i):str(calendar.month_name[i]) for i in df.month.unique()},
						step= None
					)
				], style= {'width':'75%'})

			], style= {})
			
		]),

		html.Br(),

	], style={})

], style= {'width':'100%','backgroundColor':'white'})