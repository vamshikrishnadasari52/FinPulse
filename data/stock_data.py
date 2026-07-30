import yfinance as yf


def get_stock_data(symbol, period):
    """
    Fetch company information and historical stock data.
    """

    stock = yf.Ticker(symbol)

    info = stock.info

    if period == "1d":
        history = stock.history(
            period="1d",
            interval="5m"
        )
    else:
        history = stock.history(
            period=period
        )

    return info, history