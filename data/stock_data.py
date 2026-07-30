import yfinance as yf


def get_stock_data(symbol, period):
    """
    Fetch company information and historical stock data.
    """

    stock = yf.Ticker(symbol)

    # Historical Data
    if period == "1d":
        history = stock.history(
            period="1d",
            interval="5m"
        )
    else:
        history = stock.history(period=period)

    # Fast information
    fast = stock.fast_info

    # Try to get detailed info
    try:
        detailed = stock.info
    except Exception:
        detailed = {}

    info = {
        "longName": detailed.get("longName", symbol),
        "currentPrice": fast.get("lastPrice"),
        "previousClose": fast.get("previousClose"),
        "marketCap": fast.get("marketCap"),
        "currency": fast.get("currency", "USD")
    }

    return info, history