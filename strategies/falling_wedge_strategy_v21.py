import numpy as np
import pandas as pd
from core.logger import log_event, log_trade, log_summary

def run_strategy_v2(data, starting_capital):
    trades = []
    capital = starting_capital
    capital_history = [capital]

    for i in range(50, len(data) - 6):
        window = data.iloc[i - 30:i]
        highs = window['High'].values
        lows = window['Low'].values

        x = np.arange(30)
        high_slope, _ = np.polyfit(x, highs, 1)
        low_slope, _ = np.polyfit(x, lows, 1)

        date = data.index[i].strftime('%Y-%m-%d')
        log_event(f"{date} | High Slope: {float(high_slope):.4f}, Low Slope: {float(low_slope):.4f}")

        # ✅ Relaxed falling wedge condition (like original)
        if high_slope < -0.02 and low_slope < 0.05:
            entry = float(data['Close'].iloc[i])
            exit = float(data['Close'].iloc[i + 5])
            profit_per_share = round(exit - entry, 2)

            shares = int(capital // entry)  # Adjusted for $1000 capital
            if shares == 0:
                continue

            trade_profit = round(profit_per_share * shares, 2)
            capital += trade_profit
            capital_history.append(capital)

            entry_date = data.index[i].strftime('%Y-%m-%d')
            trades.append({
                'Entry Date': entry_date,
                'Entry': round(entry, 2),
                'Exit': round(exit, 2),
                'Profit/Share': profit_per_share,
                'Shares': shares,
                'Trade Profit': trade_profit,
                'Capital After Trade': round(capital, 2)
            })

            log_trade(entry_date, round(entry, 2), round(exit, 2), trade_profit)

    total_trades = len(trades)
    wins = sum(t['Trade Profit'] > 0 for t in trades)
    win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0

    log_summary(total_trades, round(capital - starting_capital, 2), round(win_rate, 2))

    return trades, capital_history, win_rate
