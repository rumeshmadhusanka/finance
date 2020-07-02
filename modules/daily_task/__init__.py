import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler


class DailyTask:
    def __init__(self):
        self.companies = ["FB", "AAPL", "NFLX", "GOOG"]

    # get data from api and save todo
    def task(self):
        print("Task is running")

    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.task, trigger="interval", seconds=3)
        scheduler.start()
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    d = DailyTask()
    d.start()
    input()
