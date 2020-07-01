from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf


# def get_daily_data(company_code):
#     ticker = yf.Ticker(company_code)
#     info = ticker.info
#     ret = {
#         "open": info["open"],
#         "high": info["dayHigh"],
#         "low": info["dayLow"],
#         "close": info["previousClose"],
#         "volume": info["volume"]
#     }
#     return ret
def get_company_info(company_code):
    ticker = yf.Ticker(company_code)
    info = ticker.info
    ret = {
        "sector": info["sector"],
        "address": info["address1"],
        "symbol": info["symbol"],
        "short_name": info["shortName"]
    }
    return ret


def get_daily_data(company_code):
    ticker = yf.Ticker(company_code)
    df = ticker.history(period="100d")
    df = df.reset_index()
    df.Date = pd.to_datetime(df.Date)
    # 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'
    ret = []
    for index, row in df.iterrows():
        ret.append(row.values.tolist())
    return ret


def set_recommend_value(grade):
    if grade == "Buy":
        return 1
    elif grade == "Neutral":
        return 0
    elif grade == "Strong Buy":
        return 1.5
    elif grade == "Sell":
        return -1
    elif grade == "Strong Sell":
        return -1.5
    elif grade == "Positive":
        return 1
    elif grade == "Negative":
        return -1
    else:
        return 0


def get_recommendations(company_code, start_date=(datetime.now() - timedelta(days=200)), end_date=datetime.now()):
    ticker = yf.Ticker(company_code)
    df = ticker.recommendations
    mask = (df.index > start_date) & (df.index <= end_date)
    df = df.loc[mask]
    df = df.reset_index()
    df.Date = pd.to_datetime(df.Date)
    df['recommend'] = list(map(set_recommend_value, df['To Grade']))
    return df


if __name__ == '__main__':
    comp = "NFLX"

    # hist = get_daily_data(comp)
    # print(hist)
    # ticker = yf.Ticker(comp)
    # info = ticker.info
    # print(info)
    # recom = get_recommendations(comp)
    # print(recom.to_string())

    get_company_info(comp)
