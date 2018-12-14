# Final Project -- Stock Indexes

My final project is a two part project, both parts involving daily stock indexes but involving different methods of displaying the data. The first part takes data from a local csv file and creates a scatter plot of the data, showing the trends and similarities the data has with each other. The second part of the project involves taking real time data from a url and plotting the data in a candlestick format. The data shows the open, high, low, and close for a previous amount of days.

## Installation

I used a variety of tools for this project. I used Anaconda-Navigator with Jupyter Notebook for writing the code. Anaconda comes with a lot of relevant preinstalled packages which is very convienent. 

For this project, here are the libraries that were all used:
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly
import plotly.graph_objs as go
```

## Usage
Once you have all the needed libraries installed, it is pretty simple to run. Open your terminal or command prompt and move to the location of the file, then enter the following command:
```bash
python FinalProj.py
```
It is locally hosted on the web browser of your choosing. Go to the web browser and enter the address that your prompt told you to choose. For me, it is http://127.0.0.1:8050/. Now you should be able to see two tabs, one with the Data Derby stocks and another with the Real-time daily stock indexes.

## Requirements Met
- For the GUI, my project is an interactive website.
- I have three self-written functions, but almost all of the code is utilizing functions from the libraries. I wrote a function wrapper:
```python
@app.callback(Output('tabs-content', 'children'),
					[Input('tabs', 'value')]
			)
```
  This is a small but effective function that allows for the interaction of the tabs and changes the values so that the data    on the screen changes with the tabs.
  
  My second function I also consider the third, because it returns two different values depending on which tab is open. It will either show:
```python
def render_content(tab):
	#First tab
	if tab == 'tab-1':
		return (html.Div(className='twelve columns', children=[
			html.H3('Data Derby Indexes', style={'textAlign':'center'}),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Scatter(x=dt['Date'], 
						y=dt['W500'], 
						name='W5000'),],
					layout=go.Layout(
						title='W5000: 1971 - 2016',
						showlegend = True),))]),
		
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
```
or:
```python
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
					layout=go.Layout(showlegend=False),))]),
		html.Div(className='twelve columns', children=[
			html.H3('Amazon Stocks', style={'textAlign':'center'}),
			dcc.Graph(
				figure=go.Figure(
					data=[ go.Ohlc(x=amzn['timestamp'], 
									open=amzn['open'], 
									high=amzn['high'], 
									low=amzn['low'],
									close=amzn['close']),],
					layout=go.Layout(showlegend=False),))]))
```
  The first of these two shows the first tab data, which is the data derby indexes, the second will show the real time.

- I don't think I actually used any modules that we used in class, but I learned a lot about new modules for this project.
- This reads from both the local csv file and the url which is a csv file.
- I have exception handling for both times csv files are read, they put an error if the csv file is not functioning properly:
```python
try:
        dt = pd.read_csv('dataThon.csv', sep='\t', usecols=fields)
except:
        print('\n***CSV FILE ERROR. Take a look at your csv file path.***\n')

try:
        micdf = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=V39QMK0NXHH2RAQE&datatype=csv')
        amzn = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=V39QMK0NXHH2RAQE&datatype=csv')
        tsla = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=V39QMK0NXHH2RAQE&datatype=csv')
except:
        print('\n***URL ERROR, look at which stock didn\'t load and fix the url.***\n')
```
- My project as almost a whole was a new concept for me.

## Reflection
This project was tricky because I spent more time learning and reading rather than acutally coding. Being sick for the past four days did not make the reading easier as well. I also struggled with finding where to get online data, as Google Finance and Yahoo Finance are shut down which was my original plan. I've always been interested in data science and data manipulation better never actually tried it myself. It felt good to complete this goal because I knew it would be challenging but be something that I would find enjoyable. I want to add on to this by using the stocker library and trying to create prediction bots to figure out more ways to analyze the data.
