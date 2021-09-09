import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('time_data.csv')

data['Date'] = pd.to_datetime(data['Date'])
# convert string into datetime data
data.sort_values('Date', inplace=True)
# sort chronological
# data = data.sort_values('Date') # the same as 12: inplace replaces data=

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
