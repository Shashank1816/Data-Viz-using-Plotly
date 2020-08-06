import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# between 1 to 100 it gives us 100 integers
# Now we'll plot the graph
data=[go.Scatter(x=random_x, 
                y=random_y, 
                mode='markers',
                marker=dict(
                    size=12,
                    color='red',
                    symbol='pentagon',
                    line={'width':2}
                ))]
# Now we'll add labels and hovermodes before plotting
layout=go.Layout(title='Hello First Plot',
                 xaxis={'title':'MY X AXIS'} ,
                  yaxis=dict(title='MY Y AXIS'), 
                  hovermode='closest')
# this on eis not a list , axis take the arguments as dictionaries

# Now we'll pass the layout to the figure object which will then be passed to plot
fig= go.Figure(data=data,layout=layout)
pyo.plot(fig, filename="Scatter.html") # by default the file name is temp-plot.html but we can override it 
