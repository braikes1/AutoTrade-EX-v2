import yfinance as yf
import pandas as pd

def fetch_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end, interval='1d', auto_adjust=True)
    df.dropna(inplace=True)
    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(int)
    return df
