from modules.database import Database
from modules.yfinance_impl import get_daily_data, get_company_info

database = Database()


class Company:
    def __init__(self, company_code):
        self.company_code = company_code

    def get_daily_data(self, start_date, end_date):
        query = "select * from public.daily_price where company = %(company_code)s and date between %(start_date)s  " \
                "and %(end_date)s "
        return database.execute_query(query, {"company_code": self.company_code, "start_date": start_date,
                                              "end_date": end_date})

    def set_daily_data(self):
        query = "insert into public.daily_price(company, open, high, low, close, volume, date) values (%(company)s," \
                "%(open)s,%(high)s,%(low)s,%(close)s,%(volume)s,%(date)s) on conflict do nothing "

        data = get_daily_data(self.company_code)
        for each in data:
            database.execute_update(query, {"company": self.company_code,
                                            "open": each[1],
                                            "high": each[2],
                                            "low": each[3],
                                            "close": each[4],
                                            "volume": each[5],
                                            "date": each[0]
                                            })

    def get_company_info(self):
        query = "select sector,address,symbol,short_name from public.company"
        return database.execute_query(query)

    def set_company_info(self):
        query = "insert into public.company(code,sector, address, symbol, short_name) values (%(code)s,%(sector)s," \
                "%(address)s,%(symbol)s,%(short_name)s) on conflict(code) do update set code= %(code)s, " \
                "sector= %(sector)s, address= %(address)s,symbol= %(symbol)s,short_name= %(short_name)s where " \
                "company.code= %(code)s "
        info = get_company_info(self.company_code)
        database.execute_update(query, {"code": self.company_code, "sector": info['sector'], "address": info['address'],
                                        "symbol": info['symbol'], "short_name": info['short_name']},
                                )

    def get_recommendations(self, start_date, end_date):
        query = "select * from public.recommendations where date between %(start_date)s and %(end_date)s"
        return database.execute_query(query, {"start_date": start_date, "end_date": end_date})


    def set_recommendations(self):
        pass


if __name__ == '__main__':
    d = Company("AAPL")
    # print(d.get_daily_data("2020-01-20", '2020-07-01'))
    # d.set_daily_data()
    # print(d.get_daily_data("2020-01-20", '2020-07-01'))
