from data.spy_chart_v21 import fetch_data
from strategies.falling_wedge_strategy_v21 import run_strategy_v2
from core.logger import log_event

if __name__ == "__main__":
    symbol = "SPY"
    start_date = "2024-01-01"
    end_date = "2025-01-01"
    capital = 1000

    log_event(f"🚀 Running AutoTrade EX v2.1 for {symbol} from {start_date} to {end_date}...")

    df = fetch_data(symbol, start_date, end_date)
    trades, capital_history, winrate = run_strategy_v2(df, capital)

    print("\n📌 First 5 Trades:")
    for trade in trades[:5]:
        print(trade)

    print(f"\n📊 Total Trades: {len(trades)}")
    print(f"💰 Final Capital: ${capital_history[-1]:,.2f}")
    print(f"✅ Win Rate: {winrate:.2f}%")
