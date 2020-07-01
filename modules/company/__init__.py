from modules.database import Database

database = Database()


class Company:
    def __init__(self, short_name):
        self.short_name = short_name

    def get_daily_data(self):
        return database.execute_query("Select * from ")

    def set_daily_data(self, data):
        pass

    def get_company_info(self):
        pass

    def set_company_info(self):
        pass

    def get_recommendations(self, start_date, end_date):
        pass

    def set_recommendations(self):
        pass


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
