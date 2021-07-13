import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('loads.csv')
df2 = pd.read_csv('lanes.csv')
df['text'] = df['order_number']

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
# df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)
fig = go.Figure()
fig.add_trace(go.Scattergeo(
        lon = df['first_stop.location.coordinates.lon'],
        lat = df['first_stop.location.coordinates.lat'],
        text = df['text'],
        mode = 'markers'
        # marker_color = df['cnt'],
        ))
fig.add_trace(go.Scattergeo(
        lon = df['last_stop.location.coordinates.lon'],
        lat = df['last_stop.location.coordinates.lat'],
        text = df['text'],
        mode = 'markers'
        # marker_color = df['cnt'],
        ))

for i in range(len(df)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df['first_stop.location.coordinates.lon'][i], df['last_stop.location.coordinates.lon'][i]],
            lat = [df['first_stop.location.coordinates.lat'][i], df['last_stop.location.coordinates.lat'][i]],
            mode = 'lines',
            line = dict(width = df['booked_cost'][i]/df['last_stop.stop_miles'][i], color = 'pink'),
            text = df['booked_cost'][i]/df['last_stop.stop_miles'][i],
            opacity = 0.2,
        )
    )
# fig.add_trace(go.Scattergeo(
#         lon = df2['first_stop.coordinates.lon'],
#         lat = df2['first_stop.coordinates.lat'],
#         text = df2['ml_predictions.geo_adjuster_model.baseline_value_exp_smoothed_rpm'],
#         mode = 'markers'
#         # marker_color = df['cnt'],
#         ))
# fig.add_trace(go.Scattergeo(
#         lon = df2['last_stop.coordinates.lon'],
#         lat = df2['last_stop.coordinates.lat'],
#         text = df2['ml_predictions.geo_adjuster_model.baseline_value_exp_smoothed_rpm'],
#         mode = 'markers'
#         # marker_color = df['cnt'],
#         ))

# originLat = [40.31]
# originLon=[-74.51]
# destinationLat=[36.07]
# destinationLon=[-79.82]

originLat = 40.31
originLon=-74.51
destinationLat=36.07
destinationLon=-79.82


# fig.add_trace(go.Scattergeo(
#         lon = originLon,
#         lat = originLat,
#         text = df['text'],
#         mode = 'markers'
#         # marker_color = df['cnt'],
#         ))
# fig.add_trace(go.Scattergeo(
#         lon = destinationLon,
#         lat = destinationLat,
#         text = df['text'],
#         mode = 'markers'
#         # marker_color = df['cnt'],
#         ))

fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [originLon, destinationLon],
            lat = [originLat, destinationLat],
            mode = 'markers + lines',
            line = dict(width = 5,color = 'blue'),
            opacity = 0.2,
        )
    )



fig.update_layout(
        title = 'Load and Lanes Analytics',
        geo_scope='usa',
    )


fig.show()