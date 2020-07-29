from django.db import models

class User(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  real_name = models.CharField(max_length=50)
  tz = models.CharField(max_length=100)

  class Meta:
    db_table = "user_details"

class ActivityPeriod(models.Model):
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  user = models.ForeignKey('User', default=1, on_delete=models.CASCADE)

  class Meta:
    db_table = "activity_periods"
