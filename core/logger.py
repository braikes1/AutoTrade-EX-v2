import os
import logging
from datetime import datetime

# Create the logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log filename based on the current date
log_filename = os.path.join(LOG_DIR, f"autotrade_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the logger
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_event(message):
    logging.info(message)
    print("📌", message)

def log_trade(entry_date, entry, exit, profit):
    message = f"TRADE - Entry Date: {entry_date}, Entry: {entry}, Exit: {exit}, Profit: {profit}"
    logging.info(message)

def log_summary(total_trades, total_profit, winrate):
    message = (
        f"SUMMARY - Total Trades: {total_trades}, "
        f"Total Profit: ${total_profit}, Win Rate: {winrate}%"
    )
    logging.info(message)
