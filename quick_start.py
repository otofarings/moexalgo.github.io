import moexalgo.session
from moexalgo import Market, Ticker
import pandas as pd

username = ""
password = ""

moexalgo.session.authorize(username, password)

def _generator_to_dataframe(generator_data) -> pd.DataFrame:
    return pd.DataFrame(generator_data)

# Акции SBER
sber = Ticker('SBER')

# Все акции
stocks = Market('stocks')

# Свечи по акциям SBER за период
sber_candles = _generator_to_dataframe(sber.candles(date='2023-10-10', till_date='2023-10-18', period='10m'))
print("SBER Candles:")
print(sber_candles.head())

# Данные по акциям SBER за период
sber_tradestats = _generator_to_dataframe(sber.tradestats(date='2023-10-10', till_date='2023-10-18'))
print("\nSBER Trade Stats:")
print(sber_tradestats.head())

# Данные по всем акциям за дату
all_stocks_tradestats = _generator_to_dataframe(stocks.tradestats(date='2023-10-10'))
print("\nAll Stocks Trade Stats:")
print(all_stocks_tradestats.head())

# Данные по акциям SBER за период
sber_orderstats = _generator_to_dataframe(sber.orderstats(date='2023-10-10', till_date='2023-10-18'))
print("\nSBER Order Stats:")
print(sber_orderstats.head())

# Данные по всем акциям за дату
all_stocks_orderstats = _generator_to_dataframe(stocks.orderstats(date='2023-10-10'))
print("\nAll Stocks Order Stats:")
print(all_stocks_orderstats.head())

# Данные по акциям SBER за период
sber_obstats = _generator_to_dataframe(sber.obstats(date='2023-10-10', till_date='2023-10-18'))
print("\nSBER Order Book Stats:")
print(sber_obstats.head())

# Данные по всем акциям за дату
all_stocks_obstats = _generator_to_dataframe(stocks.obstats(date='2023-10-10'))
print("\nAll Stocks Order Book Stats:")
print(all_stocks_obstats.head())
