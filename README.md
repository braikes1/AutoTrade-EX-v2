# AutoTrade EX v2

AutoTrade EX v2 is a contract-based automated trading system that detects and trades falling wedge breakout patterns using historical stock data. This version emphasizes modularity, realistic trading simulations, and future readiness for AI optimization and options trading.

## Features

- Falling wedge detection using linear regression slope analysis
- Contract-based trading simulation (100-share lots)
- Modular folder structure for scalable development
- Backtesting with result logging
- Streamlit frontend for visual review of trades
- Launchable via batch script for convenience

## Folder Structure (Overview)

- `.vscode/` - VS Code settings
- `backtests/` - Strategy testing scripts
- `core/` - Core utilities like logging
- `data/` - Local data fetching or caching
- `frontend/` - Streamlit frontend app
- `logs/` - Daily trade log files
- `strategies/` - Trading strategy logic (v2.1)
- `visualization/` - Chart plotting utilities
- `launch_autotrade_v2.bat` - Batch file for launching app on Windows
- `main.py` - Main entry point script
- `README.md` - Project documentation

## Usage

1. Clone the repository:
   git clone https://github.com/your-username/AutoTrade-EX-v2.git

2. Navigate into the folder:
   cd AutoTrade-EX-v2

3. Run a backtest manually:
   python backtests/test_strategy_v21.py

4. Or launch the Streamlit frontend:
   streamlit run frontend/app.py

5. Or double-click the batch file (Windows):
   launch_autotrade_v2.bat

## Future Development

- Add real options pricing with Yahoo Finance or brokerage APIs
- Implement 0DTE (same-day) and multi-day option strategy simulations
- Train AI model for signal filtering and trade ranking
- Build an installable desktop and mobile app version

## License

This project is under active development. For private use or collaboration inquiries, please contact the repository owner.