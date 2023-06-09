import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def add_sensor_subplot(fig, df, row, col):
    # Define colors for traces
    colors = ["black", "grey"]

    # Add Sensor 'Reading' line (LAeq)
    fig.add_trace(
        go.Scatter(x=df['datetimestamp'], y=df['Reading'], mode="lines", name="Reading", line=dict(color=colors[0])),
        row=row, col=col
    )

    #  Add min/max shaded boundaries (if sensor data available)
    if 'Maximum' in df.columns and 'Minimum' in df.columns:
        fig.add_trace(
            go.Scatter(x=df['datetimestamp'], y=df['Maximum'], mode="lines", name="Maximum", line=dict(color=colors[1])),
            row=row, col=col
        )
        fig.add_trace(
            go.Scatter(x=df['datetimestamp'], y=df['Minimum'], mode="lines", name="Minimum", fill='tonexty', fillcolor='rgba(0, 0, 0, 0.3)', line=dict(color=colors[1])),
            row=row, col=col
        )

    # Add red line: y 80Db
    fig.add_shape(
        type="line",
        x0=df['datetimestamp'].min(),
        y0=80,
        x1=df['datetimestamp'].max(),
        y1=80,
        line=dict(color="red", dash="dash"),
        row=row,
        col=col
    )

    # Update x-axis properties
    fig.update_xaxes(
        tickangle=0,
        tickformat="%d/%m/%Y %H:%M",  # tickformat="%d/%m/%Y %H:%M",
        row=row,
        col=col,
        range=[df['datetimestamp'].min(), df['datetimestamp'].max()]  # Set x-axis range
    )

    # Update y-axis properties
    fig.update_yaxes(range=[0, 105], row=row, col=col)

    return fig


# Data
df_site1 = pd.read_csv('../data/GrosvenorSquare_11440N05_Export.csv')
# Normalise df
df_site1 = df_site1.rename(columns={'Category': 'datetimestamp'})
df_site1 = df_site1.sort_values('datetimestamp')

df_site2 = pd.read_csv('../data/CundyStreetQuarter_data-sample_10294-hourly-averages.csv')
# Normalise df
df_site2['datetimestamp'] = pd.to_datetime(df_site2['Date'] + ' ' + df_site2['Start Time'])
df_site2['Reading'] = df_site2['Average LAeq']
df_site2 = df_site2[['datetimestamp', 'Reading']]
df_site2 = df_site2.sort_values('datetimestamp')

nRows = 2
nCols = 1

# Create subplots
fig = make_subplots(rows=nRows,
                    cols=nCols,
                    # vertical_spacing=0.1,
                    # horizontal_spacing=1,
                    x_title='Date & Time',
                    y_title='Decibel (LAeq 1-hour)',
                    subplot_titles=("Grosvenor-Square Sensor-1", "Cundy-Street-Quarter Sensor-1"))


# Add traces for each Site
fig = add_sensor_subplot(fig, df_site1, row=1, col=1)
fig = add_sensor_subplot(fig, df_site2, row=2, col=1)

# Set layout properties
fig.update_layout(
    height=600,
    title="Decibel Readings (1 hour LAeq)",
    xaxis=dict(title="Date and Time"),
    yaxis=dict(title="Decibel (dB)")
)

# Display the chart
fig.show()
