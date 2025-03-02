from django_cron import CronJobBase, Schedule
from datetime import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Runs every 60 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.my_cron_job'  # Unique identifier

    def do(self):
        # Your scheduled task logic
        print(f"Cron job executed at {datetime.now()}")
