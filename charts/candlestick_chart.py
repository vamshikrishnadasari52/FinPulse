import plotly.graph_objects as go


def create_candlestick_chart(history):

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=history.index,
            open=history["Open"],
            high=history["High"],
            low=history["Low"],
            close=history["Close"],
            name="Candlestick"
        )
    )

    fig.update_layout(
        title="Candlestick Chart",
        template="plotly_white",
        height=600,
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig