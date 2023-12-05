import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import MetaTrader5 as mt5
import pytz
import pandas as pd
import time
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from  datetime import datetime

if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime.now()
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, utc_from,20)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
  rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
  rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
# display data
print("\nDisplay dataframe with data")
#rates_frame['RSI'] = tb.RSI(rates_frame['close'], timeperiod = 10)
print(rates_frame)
df = rates_frame

import pandas as pd
import MetaTrader5 as mt5  # Assuming you have a MetaTrader5 library

# Sample DataFrame
# Make sure your DataFrame has 'time' and 'close' columns
# rates_frame = ...

def detect_engulfing_pattern(df):
    df['engulfing_pattern'] = None  # Add a new column to mark engulfing patterns

    for i in range(1, len(df)):
        current_close = df['close'][i]
        previous_close = df['close'][i - 1]

        if current_close > previous_close and df['open'][i - 1] > df['close'][i - 1] and df['open'][i] < df['close'][i]:
            df.at[i, 'engulfing_pattern'] = 'Bullish Engulfing'

        elif current_close < previous_close and df['open'][i - 1] < df['close'][i - 1] and df['open'][i] > df['close'][i]:
            df.at[i, 'engulfing_pattern'] = 'Bearish Engulfing'

    return df

# Assuming 'rates_frame' is your DataFrame
df = detect_engulfing_pattern(df)

# Display DataFrame with engulfing patterns
print("\nDisplay dataframe with engulfing patterns")
print(df[['time', 'open', 'high', 'low', 'close', 'engulfing_pattern']])


# Plotting
plt.figure(figsize=(10, 6))

# Plot candlestick chart
plt.plot(df['time'], df['open'], color='black', label='Open', linestyle='dashed')
plt.plot(df['time'], df['close'], color='black', label='Close', linestyle='dashed')
plt.vlines(df['time'], ymin=df['low'], ymax=df['high'], color='black', linewidth=1)

# Highlight bullish engulfing patterns
bullish_engulfing = df[df['engulfing_pattern'] == 'Bullish Engulfing']
plt.scatter(bullish_engulfing['time'], bullish_engulfing['close'], color='green', marker='^', label='Bullish Engulfing')

# Highlight bearish engulfing patterns
bearish_engulfing = df[df['engulfing_pattern'] == 'Bearish Engulfing']
plt.scatter(bearish_engulfing['time'], bearish_engulfing['close'], color='red', marker='v', label='Bearish Engulfing')

plt.title('Candlestick Chart with Engulfing Patterns for EURUSD TF H1')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

