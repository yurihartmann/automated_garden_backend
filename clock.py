from apscheduler.schedulers.blocking import BlockingScheduler

from scheduling_tasks.add_sensor import add_sensor

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    add_sensor()

sched.start()
