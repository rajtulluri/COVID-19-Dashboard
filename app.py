"""
Main App file for the dashboard. 
The App file contains the callback functions to maintain interactivity of the webpage.
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
from layouts import *
from database import read_dataset


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets= external_stylesheets)
server = app.server
app.layout = page_layout


@app.callback(
	Output('line-total-cases','figure'),
	[Input('country-name','value'),
	Input('scale-type','value'),
	Input('date-slider','value')]
	)
def update_total_case_graph(country, scale, month):
	"""
	Update line chart for total cases trend based on 
	country, scale and month chosen.

	parameter:
		country: str.
		Specify country.

		scale: Linear or Log.
		Scale of the line chart.

		month: int.
		Month in int format. Acts as upper bound
		to filter data.

	returns:
		figure: go.Figure Object.
		Figure object of the chart.
	"""

	country_df = read_dataset(country)
	country_df = country_df[country_df.month <= month]

	if scale == 'Log':

		country_df.total_cases = np.log10(country_df.total_cases)

	data= [
		go.Scatter(
			x= country_df.date,
			y= country_df.total_cases,
			hovertemplate= 'Total cases reported: %{y:.0f}<extra></extra>',
			mode= 'lines',
			line= dict(color='cadetblue', width= 3.5)
		)
	]

	layout= go.Layout(
		title= {'text':'<b>Total cases reported in the country - '+country.capitalize()+'</b>', 'x':0.5, 'y':0.95},
		yaxis= { 'showticklabels':False},
		xaxis= {'showgrid':False},
		paper_bgcolor= '#F8F8F8',
		plot_bgcolor= '#F8F8F8',	
		margin= dict(l=38,b=32,t=30,r=45)
	)

	return {
		'data': data,
		'layout':layout
	}


@app.callback(
	Output('bar-daily-cases', 'figure'),
	[Input('country-name','value'),
	Input('date-slider','value')]
	)
def update_daily_case_graph(country, month):
	"""
	Update bar chart for daily cases based on 
	country, scale and month chosen.

	parameter:
		country: str.
		Specify country.

		month: int.
		Month in int format. Acts as upper bound
		to filter data.

	returns:
		figure: go.Figure Object.
		Figure object of the chart.
	"""

	country_df = read_dataset(country)
	country_df = country_df[country_df.month <= month]

	data= [
		go.Bar(
			x= country_df.date,
			y= abs(country_df.daily_cases),
			hovertemplate= 'Cases reported: %{y:.0f}<extra></extra>',
			marker= dict(color= 'mediumaquamarine')
		)
	]

	layout = go.Layout(
		title= {'text':'<b>Daily cases reported in the country - '+country.capitalize()+'</b>', 'x':0.5,'y':0.95},
		yaxis= {'showticklabels':False},
		xaxis= {'showgrid':False},
		paper_bgcolor= '#F8F8F8',
		plot_bgcolor= '#F8F8F8',
		margin= dict(l=38,b=32,t=30,r=45)
	)

	return {
		'data': data,
		'layout':layout
	}


@app.callback(
	Output('line-total-deaths','figure'),
	[Input('country-name','value'),
	Input('scale-type','value'),
	Input('date-slider','value')]
	)
def update_total_deaths_graph(country, scale, month):
	"""
	Update line chart for total deaths trend based on 
	country, scale and month chosen.

	parameter:
		country: str.
		Specify country.

		scale: Linear or Log.
		Scale of the line chart.

		month: int.
		Month in int format. Acts as upper bound
		to filter data.

	returns:
		figure: go.Figure Object.
		Figure object of the chart.
	"""

	country_df = read_dataset(country)
	country_df = country_df[country_df.month <= month]

	if scale == 'Log':

		country_df.total_deaths = np.log10(country_df.total_deaths)


	data= [
		go.Scatter(
			x= country_df.date,
			y= country_df.total_deaths,
			mode= 'lines',
			line= dict(color='#17becf',width= 3.5),
			hovertemplate= 'Total deaths reported: %{y:.0f}<extra></extra>'
		)
	]

	layout= go.Layout(
		title= {'text':'<b>Total Deaths reported in the country - '+country.capitalize()+'</b>', 'x':0.5,'y':0.95},
		yaxis= {'showticklabels':False},
		xaxis= {'showgrid':False},
		paper_bgcolor= '#F8F8F8',
		plot_bgcolor= '#F8F8F8',
		margin= dict(l=38,b=32,t=30,r=45)
	)

	return {
	'data': data,
	'layout':layout
	}


@app.callback(
	Output('bar-daily-deaths','figure'),
	[Input('country-name','value'),
	Input('date-slider','value')]
	)
def update_daily_deaths_graph(country, month):
	"""
	Update line chart for total cases trend based on 
	country, scale and month chosen.

	parameter:
		country: str.
		Specify country.

		month: int.
		Month in int format. Acts as upper bound
		to filter data.

	returns:
		figure: go.Figure Object.
		Figure object of the chart.
	"""

	country_df = read_dataset(country)
	country_df = country_df[country_df.month <= month]

	return {
		'data': [dict(
			x= country_df.date,
			y= abs(country_df.daily_deaths),
			type= 'bar',
			hovertemplate= 'Deaths reported: %{y:.0f}<extra></extra>',
			marker= {'color':'coral'}
		)],
		'layout':dict(
			title= {'text':'<b>Daily Deaths reported in the country - '+country.capitalize()+'</b>', 'x':0.5,'y':0.95},
			yaxis= {'showticklabels':False},
			xaxis= {'showgrid':False},
			paper_bgcolor= '#F8F8F8',
			plot_bgcolor= '#F8F8F8',
			margin= dict(l=38,b=32,t=30,r=45)
		)
	}


@app.callback(
	Output('pie-active-cases','figure'),
	[Input('country-name','value')]
	)
def update_cases_pie(country):
	"""
	Update pie chart for showing percentages of active cases

	parameters:
		country: str.
		Specify country.

	returns: 
		figure: go.Figure object.
		A Figure object for the chart.
	"""

	if country == 'us':
		country = 'United States'
	elif country == 'saudi-arabia':
		country = 'Saudi Arabia'
	else:
		country = country.capitalize()


	country_stats = overall_df[overall_df.country == country]
	total_cases = country_stats.total_cases.values[0]
	active_cases = total_cases - (country_stats.total_deaths.values[0] + country_stats.total_recoveries.values[0])
	resultant_cases = total_cases - active_cases

	data= [
		go.Pie(
			values= [resultant_cases, active_cases],
			type= 'pie',
			labels= ['Cases with outcome', 'Active cases'],
			hovertemplate= '%{label}:%{percent}<extra></extra>',
			marker= dict(colors= ['#009999', '#ff9933'], line= dict(width=1)),
			hole=0.25
		)
	]

	layout= go.Layout(
		title= {'text':'<b>Active cases in '+country+'</b>','y':0.01},
		height= 210,
		width= 240,
		showlegend= False,
		paper_bgcolor= '#F8F8F8',
		margin= dict(l=23,b=28,t=15,r=33)
	)

	return {
		'data':data,
		'layout':layout
	}


@app.callback(
	Output('pie-recovered-cases','figure'),
	[Input('country-name','value')]
	)
def update_recovered_pie(country):
	"""
	Update pie chart for showing percentages of recovered cases

	parameters:
		country: str.
		Specify country.

	returns: 
		figure: go.Figure object.
		A Figure object for the chart.
	"""

	if country == 'us':
		country = 'United States'
	elif country == 'saudi-arabia':
		country = 'Saudi Arabia'
	else:
		country = country.capitalize()


	country_stats = overall_df[overall_df.country == country]
	total_cases = country_stats.total_cases.values[0]
	recovered_cases = country_stats.total_recoveries.values[0]
	resultant_cases = total_cases - recovered_cases

	data= [
		go.Pie(
			values= [resultant_cases, recovered_cases],
			type= 'pie',
			labels= ['Cases without outcome', 'Recovered cases'],
			hovertemplate= '%{label}:%{percent}<extra></extra>',
			marker= dict(colors= ['crimson', 'powderblue'], line= dict(width=1)),
			hole=0.25
		)
	]

	layout= go.Layout(
		title= {'text':'<b>Recoveries in '+country+'</b>','y':0.01},
		height= 210,
		showlegend= False,
		paper_bgcolor= '#F8F8F8',
		margin= dict(l=13,b=28,t=15,r=13)
	)

	return {
		'data':data,
		'layout':layout
	}


@app.callback(
	Output('pie-death-cases','figure'),
	[Input('country-name','value')]
	)
def update_death_pie(country):
	"""
	Update pie chart for showing percentages of deaths

	parameters:
		country: str.
		Specify country.

	returns: 
		figure: go.Figure object.
		A Figure object for the chart.
	"""

	if country == 'us':
		country = 'United States'
	elif country == 'saudi-arabia':
		country = 'Saudi Arabia'
	else:
		country = country.capitalize()


	country_stats = overall_df[overall_df.country == country]
	total_cases = country_stats.total_cases.values[0]
	death_cases = country_stats.total_deaths.values[0]
	resultant_cases = total_cases - death_cases

	data= [
		go.Pie(
			values= [resultant_cases, death_cases],
			type= 'pie',
			labels= ['Remaining cases', 'Death cases'],
			hovertemplate= '%{label}:%{percent}<extra></extra>',
			marker= dict(colors= ['plum', '#7f7f7f'], line= dict(width=1)),
			hole=0.25
		)
	]

	layout= go.Layout(
		title= {'text':'<b>Deaths in '+country+'</b>','y':0.01},
		height= 210,
		showlegend= False,
		paper_bgcolor= '#F8F8F8',
		margin= dict(l=13,b=28,t=15,r=13)	
	)

	return {
		'data':data,
		'layout':layout
	}


@app.callback(
	Output('daily-case-bullet','figure'),
	[Input('country-name','value')]
)
def update_case_bullet(country):
	"""
	Update Indicator for the cases reported today 
	as compared to yesterday.

	parameters:
		country: str.
		Specify country.

	returns:
		figure: go.Figure object.
		A figure object for the chart.
	"""

	country_df = read_dataset(country)

	data= [
		go.Indicator(
			mode= 'number+delta',
			value= country_df.iloc[-1].daily_cases,
			delta= {'reference':country_df.iloc[-2].daily_cases}
		)
	]	

	layout= go.Layout(
		title= {'text':'Reported cases','y':0.95},
		margin= dict(l=13,b=8,t=13,r=13),
		height= 100,
		width= 172,
		paper_bgcolor= '#F8F8F8'
	)

	return {
		'data':data,
		'layout':layout
	}


@app.callback(
	Output('death-bullet','figure'),
	[Input('country-name','value')]
)
def update_death_bullet(country):
	"""
	Update Indicator for the death cases reported today 
	as compared to yesterday.

	parameters:
		country: str.
		Specify country.

	returns:
		figure: go.Figure object.
		A figure object for the chart.
	"""

	country_df = read_dataset(country)

	data= [
		go.Indicator(
			mode= 'number+delta',
			value= country_df.iloc[-1].daily_deaths,
			delta= {'reference':country_df.iloc[-2].daily_deaths}
		)
	]	

	layout= go.Layout(
		title= {'text':'Deaths','y':0.95},
		margin= dict(l=13,b=8,t=13,r=13),
		height= 100,
		width= 172,
		paper_bgcolor= '#F8F8F8'
	)

	return {
		'data':data,
		'layout':layout
	}	


@app.callback(
	Output('death-rate','figure'),
	[Input('country-name','value')]
)
def update_death_rate(country):
	"""
	Update Indicator for the death rate
	in the country.

	parameters:
		country: str.
		Specify country.

	returns:
		figure: go.Figure object.
		A figure object for the chart.
	"""

	country_df = read_dataset(country)
	curr_rate = (country_df.iloc[-1].total_deaths / country_df.iloc[-1].total_cases) * 100
	prev_rate = (country_df.iloc[-2].total_deaths / country_df.iloc[-2].total_cases) * 100

	data= [
		go.Indicator(
			mode= 'number+delta',
			value= curr_rate,
			number= {'suffix':'%'},
			delta= {'reference':prev_rate}
		)
	]	

	layout= go.Layout(
		title= {'text':'Death rate','y':0.95},
		margin= dict(l=13,b=8,t=13,r=13),
		height= 100,
		width= 172,
		paper_bgcolor= '#F8F8F8'
	)

	return {
		'data':data,
		'layout':layout
	}	


@app.callback(
	Output('positive-rate','figure'),
	[Input('country-name','value')]
)
def update_case_rate(country):
	"""
	Update Indicator for the active cases rate 
	in the country.

	parameters:
		country: str.
		Specify country.

	returns:
		figure: go.Figure object.
		A figure object for the chart.
	"""

	country_df = read_dataset(country)
	curr_rate = (country_df.iloc[-1].active_cases / country_df.iloc[-1].total_cases) * 100
	prev_rate = (country_df.iloc[-2].active_cases / country_df.iloc[-2].total_cases) * 100

	data= [
		go.Indicator(
			mode= 'number+delta',
			value= curr_rate,
			number= {'suffix':'%'},
			delta= {'reference':prev_rate}
		)
	]	

	layout= go.Layout(
		title= {'text':'Infected rate','y':0.95},
		margin= dict(l=13,b=8,t=13,r=13),
		height= 100,
		width= 172,
		paper_bgcolor= '#F8F8F8'
	)

	return {
		'data':data,
		'layout':layout
	}	


if __name__ == '__main__':

	app.title= 'COVID-19 Dashboard'
	app.run_server(debug=True, host= '127.0.0.1',port=5000)