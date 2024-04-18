from moexalgo import Market, Ticker
import pandas as pd
from pandas import DataFrame
import moexalgo.session
from enum import Enum
from typing import List


class MOEXTimePeriods(Enum):
    ONE_MINUTE = '1m'
    TEN_MINUTES = '10m'
    ONE_HOUR = '1h'
    ONE_DAY = 'D'
    ONE_WEEK = 'W'
    ONE_MONTH = 'M'
    ONE_QUARTER = 'Q'


class AlgoPack:
    def __init__(self, username: str, password: str):
        moexalgo.session.authorize(username, password)

    @staticmethod
    def _generator_to_dataframe(generator_data) -> pd.DataFrame:
        return pd.DataFrame(generator_data)

    @staticmethod
    def _handle_error(error):
        error_message = f"Error occurred: {error}"
        raise Exception(error_message)

    def get_candles(self, ticker: str, date: str, till_date: str, period: MOEXTimePeriods) -> pd.DataFrame:
        stock = Ticker(ticker)
        try:
            candles_data = stock.candles(date=date, till_date=till_date, period=period.value)
            return self._generator_to_dataframe(candles_data)
        except Exception as e:
            self._handle_error(e)

    def get_tradestats(self, ticker: str, date: str, till_date: str) -> pd.DataFrame:
        stock = Ticker(ticker)
        try:
            tradestats_data = stock.tradestats(date=date, till_date=till_date)
            return self._generator_to_dataframe(tradestats_data)
        except Exception as e:
            self._handle_error(e)

    def get_orderstats(self, ticker: str, date: str, till_date: str) -> pd.DataFrame:
        stock = Ticker(ticker)
        try:
            orderstats_data = stock.orderstats(date=date, till_date=till_date)
            return self._generator_to_dataframe(orderstats_data)
        except Exception as e:
            self._handle_error(e)

    def get_obstats(self, ticker: str, date: str, till_date: str) -> pd.DataFrame:
        stock = Ticker(ticker)
        try:
            obstats_data = stock.obstats(date=date, till_date=till_date)
            return self._generator_to_dataframe(obstats_data)
        except Exception as e:
            self._handle_error(e)

    def get_tickers(self) -> List[str]:
        stocks = Market('stocks')
        return [ticker['SECID'] for ticker in stocks.tickers()]


if __name__ == "__main__":
    algo_pack = AlgoPack("Ivan.Bogomolov2@moex.com", "21Ivvaarnya26")

    all_tickers = algo_pack.get_tickers()
    print("\nAll Tickers:")
    print(all_tickers)
    
    candles_data = algo_pack.get_candles(ticker="SBER", date="2024-04-01", till_date="2024-04-11", period=MOEXTimePeriods.ONE_DAY)
    print("Candles Data:")
    print(candles_data)
    
    tradestats_data = algo_pack.get_tradestats(ticker="SBER", date="2024-04-01", till_date="2024-04-11")
    print("\nTrade Stats Data:")
    print(tradestats_data)
    
    orderstats_data = algo_pack.get_orderstats(ticker="SBER", date="2024-04-01", till_date="2024-04-11")
    print("\nOrder Stats Data:")
    print(orderstats_data)
    
    obstats_data = algo_pack.get_obstats(ticker="SBER", date="2024-04-01", till_date="2024-04-11")
    print("\nOrder Book Stats Data:")
    print(obstats_data)
