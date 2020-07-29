from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .models import ActivityPeriod

def getUserActivities(request):
  user_details = User.objects.all() #Getting all the users
  activity_periods = ActivityPeriod.objects.all() #Getting all the user activities 
  json_data = {"ok": True, "members": []}
  for user in user_details:
    user_detail = {}
    user_detail["id"] = user.id
    user_detail["real_name"] = user.real_name
    user_detail["tz"] = user.tz
    user_detail["activity_periods"] = []
    for activity in activity_periods:
      if(activity.user_id==user.id):
        activity_detail = {}
        activity_detail["start_time"] = activity.start_time.strftime("%b %d %Y %I:%M%p")
        activity_detail["end_time"] = activity.end_time.strftime("%b %d %Y %I:%M%p")
        user_detail["activity_periods"].append(activity_detail)
    json_data["members"].append(user_detail)
  return JsonResponse(json_data)

def index(request):
  return render(request, 'index.html', {})
