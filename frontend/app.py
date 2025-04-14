import streamlit as st
import pandas as pd
from datetime import date
from data.spy_chart_v21 import fetch_data
from strategies.falling_wedge_strategy_v21 import run_strategy_v2
from visualization.plot_test import plot_capital_growth

st.set_page_config(page_title="AutoTrade Dashboard", layout="wide")
st.title("📈 AutoTrade Strategy Dashboard - v2")

# --- Sidebar Inputs ---
symbol = st.text_input("Symbol", value="SPY")
date_range = st.date_input("Date Range", [date(2024, 1, 1), date(2025, 1, 1)])
capital = st.number_input("Starting Capital ($)", value=1000, step=100)

run = st.button("🚀 Run Strategy v2")

if run:
    df = fetch_data(symbol, date_range[0], date_range[1])
    trades, capital_history, winrate = run_strategy_v2(df, capital)

    st.subheader("🟧 Strategy v2: Contract-Based")
    st.write("### Total Trades Detected:", len(trades))
    st.write("📊 Bars Analyzed:", len(df))

    if trades:
        st.dataframe(pd.DataFrame(trades))
        st.subheader(f"Final Capital")
        st.subheader(f"${capital_history[-1]:,.2f}")
        st.subheader(f"Win Rate: {winrate:.1f}%")

        st.write("### 📉 Capital Growth")
        plot_capital_growth(capital_history)
    else:
        st.warning("No falling wedge entries detected in the selected range.")
        st.subheader(f"Final Capital")
        st.subheader(f"${capital:,.2f}")
        st.subheader("Win Rate: 0.0%")

# --- Footer ---
st.caption("Built with ❤️ by Bryan Raikes and Jarvis")
