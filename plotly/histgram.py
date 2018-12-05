import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

y = np.random.randn(500)
data = [go.Histogram(y=y)]

url = py.iplot(data, filename='horizontal histogram', auto_open=True)


