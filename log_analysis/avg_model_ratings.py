import pandas as pd
import plotly.graph_objects as go
import time
import numpy as np

# F1 scores
F1 = {
    'Ground Truth': 1.0,
    'GPT4V': 0.8992731048805815,
    'GPT4V@Shadow': 0.8992731048805815,
    'BLIP': 0.8222433460076046,
    'BLIP@Shadow': 0.8222433460076046,
    'GPV-1': 0.7855787476280834,
    'GPV-1@Shadow': 0.7855787476280834,
    'Random': 0.3337837837837838,
}

# Load the combined CSV
df = pd.read_csv('../Logs/trimmed_logs/all.csv')

# Exclude 'Ground Truth' and 'Random'
df = df[~df['model left'].isin(['Ground Truth', 'Random'])]

# Define the desired order
desired_order = ['GPV-1@Shadow', 'GPV-1', 'BLIP@Shadow', 'BLIP', 'GPT4V@Shadow', 'GPT4V']

# Filter dataframe based on desired order
df = df[df['model left'].isin(desired_order)]

# Calculate average scores and confidence intervals for each model
grouped_data = df.groupby('model left')['normalized_score']
average_scores = grouped_data.mean().reindex(desired_order)
conf_intervals = grouped_data.apply(lambda x: np.percentile(x, [2.5, 97.5])).reindex(desired_order)

# Extract lower and upper bounds from the MultiIndex
conf_intervals = pd.DataFrame(conf_intervals.tolist(), index=conf_intervals.index, columns=['lower', 'upper'])

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
    yaxis_title='User Rating',
    xaxis_title='Model',
    plot_bgcolor='white',
    font=dict(family='Arial', size=16),  # Increased font size
)

# Iterate over each model in the sorted order
for model in desired_order:
    # Determine color based on the presence of 'Shadow'
    color = 'green' if '@Shadow' not in model else 'red'

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

# Add a vertical line in the middle of 'GPV-1' and 'BLIP@Shadow'
fig.add_shape(
    go.layout.Shape(
        type="line",
        x0=1.5,
        x1=1.5,
        y0=0,
        y1=1,
        line=dict(color="black", width=5),
    )
)

fig.add_shape(
    go.layout.Shape(
        type="line",
        x0=3.5,
        x1=3.5,
        y0=0,
        y1=1,
        line=dict(color="black", width=5),
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=3.5,
        x1=5.5,
        y0=0,
        y1=1,
        fillcolor="lightgray",
        opacity=0.4,
        layer="below",
        line=dict(width=0),
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=1.5,
        x1=3.5,
        y0=0,
        y1=1,
        fillcolor="lightgray",
        opacity=0.1,
        layer="below",
        line=dict(width=0),
    )
)

fig.add_shape(
    go.layout.Shape(
        type="rect",
        x0=-0.5,
        x1=1.5,
        y0=0,
        y1=1,
        fillcolor="lightgray",
        opacity=0.4,
        layer="below",
        line=dict(width=0),
    )
)

fig.add_annotation(
    go.layout.Annotation(
        x=0.5,
        y=0.9,
        xref="x",
        yref="y",
        text="<b>F1 : {:.3f} </b>".format(F1['GPV-1']),
        showarrow=False,  # Set showarrow to False to remove arrows
        font=dict(size=16, color='black', family='Arial'),  # Adjust size and color
        bordercolor='black',  # Border color
        borderwidth=2,  # Border width
        opacity=0.7  # Background opacity
    )
)

fig.add_annotation(
    go.layout.Annotation(
        x=2.5,
        y=0.9,
        xref="x",
        yref="y",
        text="<b>F1 : {:.3f} </b>".format(F1['BLIP']),
        showarrow=False,  # Set showarrow to False to remove arrows
        font=dict(size=16, color='black', family='Arial'),  # Adjust size and color
        bordercolor='black',  # Border color
        borderwidth=2,  # Border width
        opacity=0.7  # Background opacity
    )
)

fig.add_annotation(
    go.layout.Annotation(
        x=4.5,
        y=0.9,
        xref="x",
        yref="y",
        text="<b>F1 : {:.3f} </b>".format(F1['GPT4V']),
        showarrow=False,  # Set showarrow to False to remove arrows
        font=dict(size=16, color='black', family='Arial'),  # Adjust size and color
        bordercolor='black',  # Border color
        borderwidth=2,  # Border width
        opacity=0.7  # Background opacity
    )
)



fig.update_layout(
        width=800,
        height=600
)

# Show the figure
fig.show()

# Save the figure as a PDF
fig.write_image('../Paper files/' + 'all_model_scores.pdf', format='pdf')
time.sleep(0.5)
fig.write_image('../Paper files/' + 'all_model_scores.pdf', format='pdf')
