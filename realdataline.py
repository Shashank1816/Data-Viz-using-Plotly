import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('SourceData/nst-est2017-alldata.csv')
print(df.head())
# We can see in the output that there are 5 rows and 121 columns
# This is a US census data
# Now we'll filter the data
df2=df[df['DIVISION']== '1']
print(df2.head())
df2.set_index('NAME',inplace=True)
print(df2.head())

# But we just want the Population data, so we'll filter out the data for just population data
list_of_pop_col=[col for col in df2.columns if col.startswith('POP')]
df2=df2[list_of_pop_col]
print(df2.head())
print("Shape of the dataframe id : {}".format(df2.shape))

# So Now we have 6 New England main states and their population data for 10 years 2010 to 2017.
# Now we'll built up the list comprehension
data=[go.Scatter(x=df2.columns,
                y=df2.loc[name],
                mode='lines',
                name=name
                )for name in df2.index]
pyo.plot(data,filename='Population_estimate.html')
