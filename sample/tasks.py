# from sample.models import SampleCount
# from celery import Celery, task
# from celery.schedules import crontab
# import datetime
# import os

# app = Celery('test_thread', broker='amqp://guest@localhost//')

# # @app.on_after_configure.connect
# # def setup_periodic_tasks(sender, **kwargs):
# #   sender.add_periodic_task(10.0, add_to_count(), name='add-every-10')

# @app.task
# def add_to_count():
#   try:
#     sc = SampleCount.objects.get(pk = 1)
#   except:
#     sc = SampleCount()
#   sc.num += 1
#   sc.save()

# app.conf.update(
#   CELERYBEAT_SCHEDULE = {
#     'add-to-count-2-sec': {
#       'task': 'tasks.add_to_count',
#       'schedule': 3,
#       'args': (16, 17)
#     },
#   },
# )


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from sample.models import TaskHistory
 
logger = get_task_logger(__name__)
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(minute='*/1')), ignore_result=True)
def scraper_example():
    logger.info("Start task")
    now = datetime.now()
    date_now = now.strftime("%d-%m-%Y %H:%M:%S")
    # Perform all the operations you want here
    result = 2+2
    # The name of the Task, use to find the correct TaskHistory object
    name = "scraper_example"
    taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
    taskhistory.history.update({date_now: result})
    taskhistory.save()
    logger.info("Task finished: result = %i" % result)