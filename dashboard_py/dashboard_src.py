import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data
df = pd.read_csv('../data/GrosvenorSquare_11440N05_Export.csv')
df = df.rename(columns={'Category': 'datetimestamp'})

# Create subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=("Site 1", "Site 2"))

# Define colors for traces
colors = ["blue", "green", "orange"]

# Add traces for the line plot with shaded boundaries
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Reading'], mode="lines", name="Reading", line=dict(color=colors[0])),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Maximum'], mode="lines", name="Maximum", line=dict(color=colors[1])),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Minimum'], mode="lines", name="Minimum", fill='tonexty', fillcolor=colors[2], line=dict(color=colors[1])),
    row=1, col=1
)

# Add traces for the line plot with shaded boundaries
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Reading'], mode="lines", name="Reading", line=dict(color=colors[0])),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Maximum'], mode="lines", name="Maximum", line=dict(color=colors[1])),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=df['datetimestamp'], y=df['Minimum'], mode="lines", name="Minimum", fill='tonexty', fillcolor=colors[2], line=dict(color=colors[1])),
    row=2, col=1
)

# Add a red dashed line at value 80
fig.add_shape(
    type="line",
    x0=df['datetimestamp'].min(),
    y0=80,
    x1=df['datetimestamp'].max(),
    y1=80,
    line=dict(color="red", dash="dash"),
    row="all",
    col="all"
)

# Update x-axis properties
fig.update_xaxes(
    tickangle=0,
    tickformat="%d/%m",  # tickformat="%d/%m/%Y %H:%M",
    row=1, col=1
)
fig.update_xaxes(
    tickangle=0,
    tickformat="%d/%m",  # tickformat="%d/%m/%Y %H:%M",
    row=2, col=1
)

# Update y-axis properties
fig.update_yaxes(range=[0, 105], row=1, col=1)
fig.update_yaxes(range=[0, 105], row=2, col=1)

# Set layout properties
fig.update_layout(
    height=600,
    title="Reading with Shaded Boundaries"
)

# Display the chart
fig.show()
