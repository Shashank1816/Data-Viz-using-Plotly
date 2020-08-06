import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# between 1 to 100 it gives us 100 integers
# Now we'll plot the graph
data=[go.Scatter(x=random_x, y=random_y, mode='markers')]

pyo.plot(data, filename="Scatter.html") # by default the file name is temp-plot.html but we can override it 