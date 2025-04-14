import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


def fetch_data(symbol="SPY", start="2023-01-01", end="2023-12-31"):
    data = yf.download(symbol, start=start, end=end, auto_adjust=True)
    data.dropna(inplace=True)
    return data


def detect_and_plot_wedge(data, index):
    window = data.iloc[index - 30:index]
    highs = window['High'].values
    lows = window['Low'].values

    x = np.arange(30)
    high_slope, high_intercept = np.polyfit(x, highs, 1)
    low_slope, low_intercept = np.polyfit(x, lows, 1)

    plt.figure(figsize=(10, 6))
    plt.plot(highs, label="Highs", color="red")
    plt.plot(lows, label="Lows", color="green")
    plt.plot(x, high_slope * x + high_intercept, label=f"High Trend ({high_slope:.2f})", linestyle="--", color="red")
    plt.plot(x, low_slope * x + low_intercept, label=f"Low Trend ({low_slope:.2f})", linestyle="--", color="green")

    plt.title(f"Wedge Detection near {data.index[index].strftime('%Y-%m-%d')}")
    plt.xlabel("Bars")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = fetch_data()
    print("✅ Data fetched. Scanning for wedges...")

    for i in range(50, len(df) - 6):
        window = df.iloc[i - 30:i]
        highs = window['High'].values
        lows = window['Low'].values

        x = np.arange(30)
        high_slope, _ = np.polyfit(x, highs, 1)
        low_slope, _ = np.polyfit(x, lows, 1)

        if high_slope < -0.1 and low_slope < 0:
            print(f"📉 Falling Wedge Detected on {df.index[i].strftime('%Y-%m-%d')}")
            detect_and_plot_wedge(df, i)
            break  # Plot just the first one for testing
