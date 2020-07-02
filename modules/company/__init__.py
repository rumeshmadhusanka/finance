from modules.database import Database
from modules.yfinance_impl import get_daily_data, get_company_info, get_recommendations

database = Database()


class Company:
    def __init__(self, company_code):
        self.company_code = company_code

    def get_daily_data(self, start_date, end_date):
        query = "select * from public.daily_price where company = %(company_code)s and date between %(start_date)s  " \
                "and %(end_date)s "
        return database.execute_query_get_dict(query, {"company_code": self.company_code, "start_date": start_date,
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
        query = "select sector,address,symbol,short_name from public.company where code=%(company_code)s"
        return database.execute_query_get_dict(query, {"company_code": self.company_code})

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
        query = "select DATE(timestamp_of_date) as date, round(avg(scalar)::numeric,1) as recommendation " \
                "from public.recommendations " \
                "where company = %(company_code)s and timestamp_of_date between %(" \
                "start_date)s and %(end_date)s group by(company, date)"
        return database.execute_query_get_dict(query, {"company_code": self.company_code,
                                              "start_date": start_date,
                                              "end_date": end_date})

    def set_recommendations(self):
        query = "insert into public.recommendations(company, timestamp_of_date, scalar) VALUES (%(company)s,%(date)s," \
                "%(scalar)s) on conflict (company,timestamp_of_date) do update set company= %(company)s," \
                "timestamp_of_date= %(date)s,scalar= %(scalar)s"
        data = get_recommendations(self.company_code)
        for each in data:
            database.execute_update(query, {
                "company": self.company_code,
                "date": each[0],
                "scalar": each[5]
            })


if __name__ == '__main__':
    d = Company("FB")
    # print(d.get_company_info())
    print(d.get_company_info())
    # d.set_recommendations()
    # print(d.get_daily_data("2020-01-20", '2020-07-01'))
    # d.set_daily_data()
    # print(d.get_daily_data("2020-01-20", '2020-07-01'))
