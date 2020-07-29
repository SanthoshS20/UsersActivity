from django.contrib import admin
from .models import User
from .models import ActivityPeriod

admin.site.register(ActivityPeriod)
admin.site.register(User)