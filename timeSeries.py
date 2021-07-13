import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('loads.csv')

fig = go.Figure()
#
# for i in range(len(df)):
#     fig.add_trace(
#         go.Scatter(
#             mode = 'markers',
#             x = df["first_stop.early_appointment"],
#             y = df['booked_cost'][i]/df['last_stop.stop_miles'][i]
#         )
#     )

fig.add_trace(
    go.Scatter(
        mode = 'markers',
        # text= df['booked_cost']/df['last_stop.stop_miles'],
        x = df["first_stop.early_appointment_ms"],
        y = df['booked_cost']/df['last_stop.stop_miles']
    )
)

fig.update_xaxes(title="First Stop Early Appointment (ms)")
fig.update_yaxes(title="RPM")
fig.update_layout(title="Time Series")
# fig.add_trace(go.Scatter(mode="markers", x=df["Date"], y=df["AAPL.Close"], name="daily"))
fig.show()