import plotly.plotly as py
import plotly.graph_objs as go


import numpy as np

dphi, dtheta = np.pi / 250.0, np.pi / 250.0
[phi, theta] = np.mgrid[0:np.pi + dphi * 1.5:dphi, 0:2 * np.pi +
                        dtheta * 1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;

# Applying the parametric equation..
r = (np.sin(m0 * phi) ** m1 + np.cos(m2 * phi) ** m3 +
     np.sin(m4 * theta) ** m5 + np.cos(m6 * theta) ** m7)
x = r * np.sin(phi) * np.cos(theta)
y = r * np.cos(phi)
z = r * np.sin(phi) * np.sin(theta)


surface = go.Surface(x=x, y=y, z=z, colorscale='Viridis')
data = [surface]
layout = go.Layout(
    title='Another Parametric Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='parametric-plot-viridis', auto_open=True)

