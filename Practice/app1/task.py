from celery import shared_task 
from time import sleep
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def my_task():
    for i in range(11):
        logger.info(f"Progress: {i}")
        sleep(1)
    return "Task Complete!"
