import MetaTrader5 as mt5
import pandas as pd
import pytz
from datetime import datetime
import talib as tb
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates  # Add this import
from mplfinance.original_flavor import candlestick_ohlc

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime.now()
# get 20 EURUSD H1 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, utc_from,72)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    rates_frame = pd.DataFrame(rates)

# convert time in seconds into the datetime format
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# Identify Doji candlestick pattern using talib
rates_frame['is_doji'] = tb.CDLDOJI(rates_frame['open'], rates_frame['high'], rates_frame['low'], rates_frame['close'])

# Filter rows where Doji pattern is present
doji_patterns = rates_frame[rates_frame['is_doji'] != 0]

# display data
print("\nDisplay dataframe with data")
print(rates_frame)
print("\nDoji Patterns:")
print(doji_patterns)

# Plotting candlestick chart with Doji patterns highlighted
fig, ax = plt.subplots(figsize=(10, 6))
candlestick_ohlc(ax, zip(mpl_dates.date2num(rates_frame['time']), rates_frame['open'], rates_frame['high'], rates_frame['low'], rates_frame['close']),
                 width=0.01, colorup='g', colordown='r')

# Highlight Doji patterns
ax.scatter(mpl_dates.date2num(doji_patterns['time']), doji_patterns['close']+0.0005, marker='X', color='b', label='Doji')

ax.xaxis_date()
ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.xticks(rotation=45)
plt.title('EURUSD Candlestick Chart with Doji Patterns')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
