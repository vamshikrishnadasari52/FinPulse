def format_market_cap(value, currency="USD"):
    if value is None:
        return "N/A"

    # -----------------------------
    # Indian Companies
    # -----------------------------
    if currency == "INR":

        crore = 10_000_000           # 1 Crore
        lakh_crore = 1_000_000_000_000   # 1 Lakh Crore

        if value >= lakh_crore:
            return f"₹{value/lakh_crore:.2f} Lakh Cr"

        elif value >= crore:
            return f"₹{value/crore:,.0f} Cr"

        else:
            return f"₹{value:,.0f}"

    # -----------------------------
    # International Companies
    # -----------------------------
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "CAD": "C$",
        "AUD": "A$",
        "HKD": "HK$"
    }

    symbol = symbols.get(currency, currency)

    trillion = 1_000_000_000_000
    billion = 1_000_000_000
    million = 1_000_000

    if value >= trillion:
        return f"{symbol}{value/trillion:.2f} T"

    elif value >= billion:
        return f"{symbol}{value/billion:.2f} B"

    elif value >= million:
        return f"{symbol}{value/million:.2f} M"

    return f"{symbol}{value:,.0f}"