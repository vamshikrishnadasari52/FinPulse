def add_indicators(history):

    history["SMA20"] = history["Close"].rolling(20).mean()

    history["SMA50"] = history["Close"].rolling(50).mean()

    history["Daily Return"] = (
        history["Close"].pct_change() * 100
    )

    return history