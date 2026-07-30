import plotly.graph_objects as go


def create_price_chart(history):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["Close"],
            mode="lines",
            name="Closing Price",
            line=dict(width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["SMA20"],
            mode="lines",
            name="20-Day SMA"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["SMA50"],
            mode="lines",
            name="50-Day SMA"
        )
    )

    fig.update_layout(
        title="Price Trend",
        template="plotly_white",
        height=600,
        xaxis_title="Date",
        yaxis_title="Price ($)"
    )

    return fig