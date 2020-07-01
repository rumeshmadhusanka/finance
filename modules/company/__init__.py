import yfinance as yf
import pandas as pd
from datetime import datetime


class Company:
    def __init__(self, short_name):
        self.short_name = short_name
        self.ticker = yf.Ticker(short_name)
        self.info = self.ticker.info
        self.recommendations = self.ticker.recommendations

    def get_daily_data(self):
        ret = {
            "open": self.info["open"],
            "high": self.info["dayHigh"],
            "low": self.info["dayLow"],
            "close": self.info["previousClose"],
            "volume": self.info["volume"]
        }
        return ret

    def get_historical_data(self, start_date, end_date):
        return self.ticker.history(start=start_date, end=end_date)

    def get_company_info(self):
        ret = {
            "sector": self.info["sector"],
            "address": self.info["address1"],
            "symbol": self.info["symbol"],
            "short_name": self.info["shortName"]

        }
        return ret

    def get_recommendations(self, start_date, end_date):
        # st = datetime.strptime(start_date, "%Y-%m-%d")
        # end = datetime.strptime(end_date, "%Y-%m-%d")
        #
        # i = pd.date_range(start_date,end_date)
        df = self.ticker.recommendations
        df.index.name = None
        df.index = pd.to_datetime(df.index)
        mask = (df.index > start_date) & (df.index <= end_date)
        df = df.loc[mask]
        return df


if __name__ == '__main__':
    c = Company("FB")
    # print(c.recommendations)
    # print(c.get_historical_data('2020-02-01','2020-04-05'))
    # print(c.info)
    # print(c.get_company_info())
    df = c.get_recommendations('2020-02-01', '2020-04-05')
    print(df.info(verbose=True))
    # print(type(df["Date"]))
    print(df.to_string())  # todo
