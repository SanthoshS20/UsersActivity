from django.core.management.base import BaseCommand
from activity.models import ActivityPeriod
from datetime import datetime
from django.utils import timezone
import pytz

class Command(BaseCommand):

    def handle(self, *args, **options):
        active_periods = []
        for user in range(5):
            for activity in range(3):
                kwargs = {
                    'user_id': "W012A3CD"+str(user),
                    'start_time': datetime(2020, 4, 11, 23, 55, 59, 342380, tzinfo=pytz.UTC),
                    'end_time': datetime(2020,4,12,14,20,6, 350000, tzinfo=pytz.UTC)
                }
                active_period = ActivityPeriod(**kwargs)
                active_periods.append(active_period)
        ActivityPeriod.objects.bulk_create(active_periods)
        self.stdout.write(self.style.SUCCESS('User Activities have been added successfully.'))