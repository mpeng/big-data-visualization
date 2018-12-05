import plotly
import plotly.plotly as py
import plotly.graph_objs as go


trace = go.Surface (
	colorscale = 'Viridis',
	z = [[3,5,8,13,32,1,2,44,33,22,56,55,24,6,8],[21,13,8,5, 5,8,13,32,1,2,44,33,22,56,55], [3,5,33,22,56,55,24,6,8,8,13,32,1,2,44]] )
data = [trace]
py.iplot( data , filename = 'basic-line', auto_open=True)
