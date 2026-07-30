import plotly.graph_objects as go


def create_returns_chart(history):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=history.index,
            y=history["Daily Return"],
            name="Daily Return (%)"
        )
    )

    fig.update_layout(
        title="Daily Returns",
        template="plotly_white",
        height=400,
        xaxis_title="Date",
        yaxis_title="Return (%)"
    )

    return fig