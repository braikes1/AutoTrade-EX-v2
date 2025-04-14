import matplotlib.pyplot as plt
import streamlit as st

def plot_capital_growth(capital_history):
    st.subheader("📈 Capital Growth Over Time")
    fig, ax = plt.subplots()
    ax.plot(capital_history, label="Capital", linewidth=2)
    ax.set_ylabel("Capital ($)")
    ax.set_xlabel("Trade #")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
