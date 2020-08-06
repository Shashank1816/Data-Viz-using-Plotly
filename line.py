import numpy as np 
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(56)

# Now we will create evenly distributed 100 points for our x-axis values
x_values=np.linspace(0,1,100)

# for y we'll create random values
y_values=np.random.randn(100)

trace0=go.Scatter(x=x_values,
                y=y_values+5,
                mode='markers',
                name='markers'
                )
trace1=go.Scatter(x=x_values,
                y=y_values,
                mode='lines',
                name='mylines'
                )
trace2=go.Scatter(x=x_values,
                y=y_values-5,
                mode='lines+markers',
                name='both'
                )
# now we'll append all these traces to the data list
data=[trace0,trace1,trace2]

# Now we'll create a layout 
layout=go.Layout(title='Line Charts',
                xaxis=dict(title='My X-Axis'),
                yaxis=dict(title='My Y-Axis')
                )
# Now we will create the figure object
fig=go.Figure(data=data, layout=layout)

# now we'll plot the graph
pyo.plot(fig,filename='Line.html')
    