import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample time series data
date_today = datetime.date.today()
days = pd.date_range(date_today, date_today + pd.DateOffset(days=9), freq='D')
values = np.random.randn(len(days))

# Create a DataFrame with the time series data
df = pd.DataFrame({'Date': days, 'Value': values})

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o')
plt.title('Sample Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()


# Calculate 7-day moving average
df['MA_7'] = df['Value'].rolling(window=7).mean()

# Plot the original data and the moving average
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Original Data', marker='o')
plt.plot(df['Date'], df['MA_7'], label='7-Day Moving Average', linestyle='--', color='orange')
plt.title('Time Series Data with 7-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


# another examples are for examples this below:

#    Time series analysis
#   To get a timestamp of any activities in an application
#    Adding posts on a blog

