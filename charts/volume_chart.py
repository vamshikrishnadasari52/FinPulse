import plotly.graph_objects as go


def create_volume_chart(history):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=history.index,
            y=history["Volume"],
            name="Volume"
        )
    )

    fig.update_layout(
        title="Trading Volume",
        template="plotly_white",
        height=400,
        xaxis_title="Date",
        yaxis_title="Volume"
    )

    return fig