from apscheduler.schedulers.blocking import BlockingScheduler
from scrape import run_spider

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    run_spider()


sched.start()