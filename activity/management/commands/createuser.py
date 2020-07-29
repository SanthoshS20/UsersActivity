from django.core.management.base import BaseCommand
from activity.models import User
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        time_zone = ["America/Los_Angeles", "Asia/Kolkata", "Kuala Lumpur"]
        names = ["Suresh", "Rajesh", "Prabu", "Priya", "Iniyavan"]
        users = []
        for user in range(5):
            kwargs = {
                'id': "W012A3CD"+str(user),
                'real_name': random.choice(names),
                'tz': random.choice(time_zone)
            }
            user = User(**kwargs)
            users.append(user)
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Users have been added successfully.'))