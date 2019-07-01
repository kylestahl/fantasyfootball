
import pandas as pd
import numpy as np


import plotly.offline as py
import plotly.graph_objs as go


# Filter on 1 player
player_id = "00-0020531"
brees = player_ppg[player_ppg.player_id == player_id].sort_values('date_time')

# Get lines for each season
data = []
for yr in brees.season_year.unique():
    that_year = brees[(brees.season_type == 'Regular') & (brees.season_year == yr)]
    data.append(
            go.Scatter(
                    x = that_year['week'],
                    y = that_year['total_points'],
                    name = str(yr)
                )
        )
# Define graph features
layout = go.Layout(
    title='Drew Brees Fantasy points',
    yaxis=dict(title='Point per Game'),
    xaxis=dict(title='Week of Season')
)

# Build figure
fig = go.Figure(data=data, layout=layout)
py.plot(fig)






