#All imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly
import plotly.graph_objs as go

#Grabbing data from data thon csv file
fields = ['Date','W500', '10YRTB', '1YRTB', '3MOTB', 'MBAA', '30YRMR']
try:
        dt = pd.read_csv('dataThon.csv', sep='\t', usecols=fields)
except:
        print('\n***CSV FILE ERROR. Take a look at your csv file path.***\n')

#Grabbing data from actual stocks
try:
        micdf = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=V39QMK0NXHH2RAQE&datatype=csv')
        amzn = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=V39QMK0NXHH2RAQE&datatype=csv')
        tsla = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=V39QMK0NXHH2RAQE&datatype=csv')
except:
        print('\n***URL ERROR, look at which stock didn\'t load and fix the url.***\n')
#Starting the web application
app = dash.Dash()


#Layout of the web application
app.layout = html.Div([
	dcc.Tabs(id='tabs', value='tab-1', children=[
		dcc.Tab(label='Data Derby', value='tab-1'),
		dcc.Tab(label='Real Stocks', value='tab-2'),
		]),
	html.Div(id='tabs-content'),
	])

#The different tabs
@app.callback(Output('tabs-content', 'children'),
					[Input('tabs', 'value')]
			)
#Function for changing info when tab is changed
def render_content(tab):
	#First tab
	if tab == 'tab-1':
		return (html.Div(className='twelve columns', children=[
			html.H3('Data Derby Indexes', style={'textAlign':'center'}),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Scatter(x=dt['Date'], 
						y=dt['W500'], 
						name='W5000'),
					],
					layout=go.Layout(
						title='W5000: 1971 - 2016',
						showlegend = True),
				)
			)
		]),
		
		html.Div(className='twelve columns', children=[
			dcc.Graph(
				figure = go.Figure(
					data=[go.Scatter(x=dt['Date'], y=dt['10YRTB'], name='10YRTB'),
						go.Scatter(x=dt['Date'], y=dt['1YRTB'], name='1YRTB'),
						go.Scatter(x=dt['Date'], y=dt['3MOTB'], name='3MOTB'),
						go.Scatter(x=dt['Date'], y=dt['MBAA'], name='MBAA'),
						go.Scatter(x=dt['Date'], y=dt['30YRMR'], name='30YRMR'),
					],
					layout=go.Layout(title='Smaller Indexes', showlegend=True),
				)
			)
		]),
		html.H5('W5000 = Wilshire 5000 Price Index', style={'textAlign':'center'}),
		html.H5('10YTRB = 10 Year Treasury Bill', style={'textAlign':'center'}),
		html.H5('1YTRB = 1 Year Treasury Bill', style={'textAlign':'center'}),
		html.H5('3MOTB = 3 Month Treasury Bill', style={'textAlign':'center'}),
		html.H5('MBAA = Moody\'s Seasonsed Baa Corporate Bond', style={'textAlign':'center'}),
		html.H5('30YRMR = 30 Year Mortgage Rate', style={'textAlign':'center'})
		)

	#Second tab
	elif tab == 'tab-2':
		return (html.Div(className='twelve columns', children=[
			html.H3('Microsoft Stocks', style={'textAlign':'center'}),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Ohlc(x=micdf['timestamp'], 
									open=micdf['open'], 
									high=micdf['high'], 
									low=micdf['low'],
									close=micdf['close']),],
					layout=go.Layout(showlegend=False),
				)
			)
		]),
		html.Div(className='twelve columns', children=[
			html.H3('Amazon Stocks', style={'textAlign':'center'}),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Ohlc(x=amzn['timestamp'], 
									open=amzn['open'], 
									high=amzn['high'], 
									low=amzn['low'],
									close=amzn['close']),
					],
					layout=go.Layout(showlegend=False),
				)
			)
		]))		#Remove parenthesis and add comma to add tesla stock
'''
		html.Div(className='twelve columns', children=[
			html.H3('Tesla Stock'),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Ohlc(x=tsla['timestamp'], 
									open=tsla['open'], 
									high=tsla['high'], 
									low=tsla['low'],
									close=tsla['close']),],
					layout=go.Layout(showlegend=False),
				)
			)
		]))
'''
#To add CSS characteristics
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#Main Function
if __name__ == '__main__':
	app.run_server(debug=True)
