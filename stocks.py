#!/usr/bin/env python3
# ========================================================================
# stocks.py
#
# Description: Display stock quotes on the Sense HAT LED.
#
# pip3 install yfinance
#
# Author: Jim Ing
# Date: 2024-08-30
# ========================================================================

#from config import sense
import yfinance as yf
import time
import argparse

# Set up the Sense HAT
#sense.clear()

# Define stock symbols
symbols = [
    'AAPL', 'ACN', 'ADBE', 'AMD', 'AMZN', 'AVGO', 'CRM', 'CSCO', 'DELL',
    'GOOGL', 'HP', 'IBM', 'INTC', 'INTU', 'META', 'MSFT', 'NFLX', 'NVDA',
    'ORCL', 'SAP', 'TSLA'
]

# Function to fetch stock data
def fetch_stock_data(symbols, debug=False):
    stock_data = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        info = stock.info

        if debug:
            print(f"Fetching data for {symbol}")

        price = info.get("regularMarketPrice") or info.get("currentPrice")
        prev_close = info.get("regularMarketPreviousClose") or info.get("previousClose")
        volume = info.get("regularMarketVolume")

        if price is not None and prev_close is not None:
            change = price - prev_close
            percent_change = (change / prev_close) * 100
        else:
            change = 0.00
            percent_change = 0.00

        stock_data[symbol] = {
            'price': price,
            'change': change,
            'percent_change': percent_change,
            'volume': volume
        }

        if debug:
            print(f"{symbol}: Price: {price}, Change: {change}, Percent Change: {percent_change:.2f}%, Volume: {volume}")

    return stock_data

# Function to display scrolling ticker on Sense HAT
def display_ticker(stock_data, debug=False):
    for symbol, data in stock_data.items():
        price = data['price']
        change = data['change']
        percent_change = data['percent_change']
        volume = data['volume']

        color = (0, 255, 0) if change >= 0 else (255, 0, 0)
        ticker_message = f"{symbol}: {price:.2f} ({change:+.2f} {percent_change:.2f}%) Vol: {volume}"
        print(ticker_message)
        #sense.show_message(ticker_message, scroll_speed=0.08, text_colour=color)
        #time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Stock Ticker on Sense HAT")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    debug = args.debug

    try:
        stock_data = fetch_stock_data(symbols, debug)
        display_ticker(stock_data, debug)
        #time.sleep(15 * 60)  # Refresh every 15 minutes

    except KeyboardInterrupt:
        #sense.clear()
        print("Done")

if __name__ == "__main__":
    main()
