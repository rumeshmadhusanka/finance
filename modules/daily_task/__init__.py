import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from modules.company import Company
from modules.config import Config


class DailyTask:
    def __init__(self):
        self.companies = Config.COMPANIES

    # get data from api and save
    def task(self):
        print("Scheduled task is running")
        try:
            for comp in self.companies:
                c = Company(comp)
                c.set_recommendations()
        except Exception as e:
            print("Error in Task", e)

    def start(self):
        try:
            scheduler = BackgroundScheduler()
            scheduler.add_job(func=self.task, trigger="interval", seconds=5)
            scheduler.start()
            # Shut down the scheduler when exiting the app
            atexit.register(lambda: scheduler.shutdown())
        except Exception as e:
            print("Error in Job Scheduler", e)


if __name__ == '__main__':
    d = DailyTask()
    d.start()
    input()
