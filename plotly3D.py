# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import plotly 
plotly.tools.set_credentials_file(username='mvfolino68', api_key='')
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

filtered_df=df

traces = []
for i in filtered_df.continent.unique():
    df_by_continent = filtered_df[filtered_df['continent'] == i]
    traces.append(go.Scatter3d(
        x=df_by_continent['gdp per capita'],
        y=df_by_continent['life expectancy'],
        z=df_by_continent['population'],
        text=df_by_continent['country'],
        mode='markers',
        opacity=0.9,
        marker={
            'size': 10,
            'line': {'width': 0.5, 'color': 'white'}
        },
        name=i
    ))
data = traces
layout = go.Layout(
                scene={  
                        'xaxis':{'type': 'linear', 'title': 'X: GDP Per Capita'},
                           'yaxis':{'title': 'Y: Life Expectancy', 'range': [20, 90]},
                           'zaxis':{'type': 'log', 'title': 'Z: Poplulation'}
                           },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            title=go.layout.Title(
            text='2007 Life Expectancy by Per Capita GDP by Population',
            xref='paper',
            x=.5, y=1)
        )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='2007 Life Expectancy by Per Capita GDP by Population')
