import streamlit as st

from data.stock_data import get_stock_data
from data.indicators import add_indicators

from charts.price_chart import create_price_chart
from charts.volume_chart import create_volume_chart
from charts.candlestick_chart import create_candlestick_chart
from charts.returns_chart import create_returns_chart

from utils.formatter import format_market_cap


# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="FinPulse",
    page_icon="📈",
    layout="wide"
)

st.title("📈 FinPulse")
st.subheader("Stock Tracker & Financial Dashboard")


# ----------------------------------------------------
# USER INPUT
# ----------------------------------------------------

symbol = st.text_input(
    "Enter Stock Symbol",
    "RELIANCE.NS"
).upper()

st.caption(
    "Examples: RELIANCE.NS, TCS.NS, INFY.NS, HDFCBANK.NS, AAPL, MSFT"
)

periods = {
    "1 Day": "1d",
    "5 Days": "5d",
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y",
    "5 Years": "5y",
    "10 Years": "10y",
    "Maximum": "max"
}

selected = st.selectbox(
    "Select Time Period",
    list(periods.keys())
)

period = periods[selected]


# ----------------------------------------------------
# BUTTON
# ----------------------------------------------------

if st.button("Get Stock Data"):

    try:

        # -----------------------------------
        # Fetch Data
        # -----------------------------------

        info, history = get_stock_data(symbol, period)

        if history.empty:
            st.error("No data found.")
            st.stop()

        history = add_indicators(history)

        company = info.get("longName", symbol)

        st.success(f"Showing data for {company}")

        st.divider()

        # -----------------------------------
        # Company Metrics
        # -----------------------------------

        col1, col2, col3 = st.columns(3)

        current_price = info.get("currentPrice")
        previous_close = info.get("previousClose")

        # Detect Currency
        currency = info.get("currency", "USD")

        currency_symbols = {
            "USD": "$",
            "INR": "₹",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CAD": "C$",
            "AUD": "A$",
            "HKD": "HK$"
        }

        currency_symbol = currency_symbols.get(currency, currency)

        market_cap = format_market_cap(
            info.get("marketCap"),
            currency
        )

        col1.metric(
            "Current Price",
            f"{currency_symbol}{current_price:,.2f}"
            if current_price is not None else "N/A"
        )

        col2.metric(
            "Previous Close",
            f"{currency_symbol}{previous_close:,.2f}"
            if previous_close is not None else "N/A"
        )

        col3.metric(
            "Market Cap",
            market_cap
        )

        st.divider()

        # -----------------------------------
        # Stock Summary
        # -----------------------------------

        st.subheader("📊 Stock Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Highest Price",
            f"{currency_symbol}{history['High'].max():,.2f}"
        )

        c2.metric(
            "Lowest Price",
            f"{currency_symbol}{history['Low'].min():,.2f}"
        )

        c3.metric(
            "Average Close",
            f"{currency_symbol}{history['Close'].mean():,.2f}"
        )

        c4.metric(
            "Total Volume",
            f"{history['Volume'].sum():,.0f}"
        )

        st.divider()

        # -----------------------------------
        # Price Trend
        # -----------------------------------

        st.subheader("📈 Price Trend")

        price_chart = create_price_chart(history)

        st.plotly_chart(
            price_chart,
            use_container_width=True
        )

        st.divider()

        # -----------------------------------
        # Candlestick Chart
        # -----------------------------------

        st.subheader("🕯️ Candlestick Chart")

        candlestick = create_candlestick_chart(history)

        st.plotly_chart(
            candlestick,
            use_container_width=True
        )

        st.divider()

        # -----------------------------------
        # Trading Volume
        # -----------------------------------

        st.subheader("📊 Trading Volume")

        volume_chart = create_volume_chart(history)

        st.plotly_chart(
            volume_chart,
            use_container_width=True
        )

        st.divider()

        # -----------------------------------
        # Daily Returns
        # -----------------------------------

        st.subheader("📉 Daily Returns")

        returns_chart = create_returns_chart(history)

        st.plotly_chart(
            returns_chart,
            use_container_width=True
        )

        st.divider()

        # -----------------------------------
        # Historical Data
        # -----------------------------------

        st.subheader("📋 Historical Data")

        display_df = history.copy()

        display_df["Daily Return"] = (
            display_df["Daily Return"].fillna(0)
        )

        st.dataframe(
            display_df.style.format({
                "Open": "{:.2f}",
                "High": "{:.2f}",
                "Low": "{:.2f}",
                "Close": "{:.2f}",
                "Volume": "{:,.0f}",
                "SMA20": "{:.2f}",
                "SMA50": "{:.2f}",
                "Daily Return": "{:.2f}%"
            }),
            use_container_width=True
        )

        csv = display_df.to_csv().encode("utf-8")

        st.download_button(
            label="📥 Download Historical Data",
            data=csv,
            file_name=f"{symbol}_historical_data.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error("Unable to fetch stock data.")

        st.exception(e)