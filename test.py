import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

df = pd.read_csv('/home/hp/Github/COVID-19-Web-Scraper/Data/covid19_india_stats.csv')
numdate = [x for x in range(0,len(df.date.unique()))]

def generate_table(dataframe, max_rows=25):

	return html.Table([
		html.Thead(
			html.Tr([html.Th(col) for col in dataframe.columns])
			),
		html.Tbody([
			html.Tr(
				[html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
				) for i in range(25)
			])
		])

app.layout = html.Div(children=[
	html.H3(children= "Hello World, I am here doing Dash!!!", style={
		'textAlign':'center',
		'color':'#009999'
		}),

	html.Div(children="""
		Dashboard test application.
		""",
		style={
		'textAlign':'center',
		'color':'#ff9933'
		}),

	dcc.Graph(
		id= 'test-graph',
		figure={
			'data':[
			{'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},
			{'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'Delhi'}
			],
			'layout':{
			'title':{'text':'<b>My first graph, shows bullshit!</b>','x':0.5}
			}
		}
	),

	dcc.Graph(
		id= 'line-graph',
		figure={
			'data':[
			{'x':[1,2,3,4,5,6,7,8],'y':[1,4,9,16,25,36,49,64],'type':'line','name':'Square line'},
			{'x':[1,2,3,4,5,6,7,8],'y':[45,67,12,34,50,8,28], 'type':'scatter', 'mode':'markers'}
			],
			'layout':{
			'title':'Line plot for testing!!'
			}
		}
	),

	generate_table(df),

	html.Br(),

	dcc.Slider(
		id= 'date-slider',
		min = numdate[0],
		max = numdate[-1],
		value = numdate[-1],
		marks= {str(dt): str(dt) for dt in df.date.unique()[::15]},
		step= 15
	),
	html.Br(),

	dcc.Graph(id='callback-example')

])

@app.callback(
	Output('callback-example','figure'),
	[Input('date-slider','value')]
	)
def update_figure(selected_date):
	filtered_df = df.iloc[:selected_date]

	return {
		'data': [dict(
				x= filtered_df.date,
				y= filtered_df.total_cases,
				mode= 'line',
				marker= {
					'size':5.5,
					# 'line':{'width':5.5,'color':'#009999'}
				},
				name= 'Total cases'
			)],

		'layout': dict(
				xaxis= {'title':'Date (2020)'},
				yaxis= {'title':'Total number of cases'}
			)
	}

if __name__ == '__main__':
	
	app.run_server(debug=True, port= 3000)