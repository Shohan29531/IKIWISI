import pandas as pd
import plotly.graph_objects as go
import time
import numpy as np

# Load the combined CSV
df = pd.read_csv('NASA-TLX.csv')

# Convert 'model left' column to string
df['model left'] = df['model left'].astype(str)

# Exclude 'Ground Truth' and 'Random'
df = df[~df['model left'].isin(['Ground Truth', 'Random'])]

# Define the desired order
desired_order = ['GPV-1@Shadow', 'GPV-1', '', ' ', 'BLIP@Shadow', 'BLIP', '  ', '   ', 'GPT4V@Shadow', 'GPT4V']

# Filter dataframe based on desired order
df = df[df['model left'].isin(desired_order)]

# Calculate average scores and confidence intervals for each model
grouped_data = df.groupby('model left')['normalized_score']
average_scores = grouped_data.mean().reindex(desired_order)

conf_intervals = grouped_data.apply(lambda x: np.percentile(x, [2.5, 97.5])).reindex(desired_order)

# Extract lower and upper bounds from the MultiIndex
conf_intervals = conf_intervals.apply(lambda x: pd.Series(x)).rename(columns={0: 'lower', 1: 'upper'})

# Create traces for horizontal lines and markers (representing mean and confidence interval)
lines = []
dots = []

# Create the layout
layout = go.Layout(
    title=dict(
        text='Average User Ratings for Different Models',
        x=0.5,  # Center align the title
        font=dict(family='Arial', size=20, color='black')  # Increased font size
    ),
    yaxis_title='Mean-Centered User Data',
    xaxis_title='Model',
    plot_bgcolor='white',
    font=dict(family='Arial', size=14),  # Increased font size
    yaxis=dict(
        showgrid=True,  # Show horizontal gridlines
        gridwidth=0.5,
        gridcolor='lightgrey',
        dtick=0.1,  # Set gridline interval
        range=[-0.7, 0.7]
    ),
)
layout['yaxis'].update(showgrid=True, gridwidth=1, gridcolor='lightgrey', zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey')

# Iterate over each model in the sorted order
for model in desired_order:
    # Determine color based on the presence of 'Shadow'
    color = 'black' if '@Shadow' not in model else 'rgb(158, 157, 157)'

    # Add a horizontal line trace for the mean
    lines.append(go.Scatter(
        x=[model, model],
        y=[conf_intervals.loc[model, 'lower'], conf_intervals.loc[model, 'upper']],
        mode='lines',
        line=dict(color=color, width=2),
        showlegend=False
    ))

    # Add a marker trace for the mean
    dots.append(go.Scatter(
        x=[model],
        y=[average_scores[model]],
        mode='markers',
        marker=dict(color=color, size=14),
        showlegend=False
    ))

# Add the lines and dots traces
fig = go.Figure(data=lines + dots, layout=layout)

# Add F1 score annotations
for model, x_pos in zip(['GPV-1', 'BLIP', 'GPT4V'], [0.5, 4.5, 8.5]):
    fig.add_annotation(
        go.layout.Annotation(
            x=x_pos,
            y=0.57,
            xref="x",
            yref="y",
            text="<b>F1 : {:.3f} </b>".format(F1[model]),
            showarrow=False,
            font=dict(size=16, color='black', family='Arial'),
            bordercolor='black',
            borderwidth=2,
            opacity=0.7,
            bgcolor='lightgrey',
        )
    )



# Update layout for width and height
fig.update_layout(
    width=600,
    height=600
)

# Show the figure
fig.show()

# Save the figure as a PDF
fig.write_image('../Paper files/' + 'all_model_scores.pdf', format='pdf')
time.sleep(0.5)
fig.write_image('../Paper files/' + 'all_model_scores.pdf', format='pdf')