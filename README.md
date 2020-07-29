# UsersActivity


## ENVIRONMENT REQUIRED TO RUN THE APPLICATION
Django - 3.0\
Python - 3.8.2\
psycopg2 - 2.8.5

## HOW TO RUN THE APPLICATION
Step 1: Create new virtual environment\
Step 2: Install Django and PostgreSQL\
Step 3: Create Database in the PgAdmin\ 
Step 4: Change the database name in the setting file\
Step 5: Make Migration\
Step 6: Run python manage.py createuser\ 
Step 7: Run python manage.py createactivity\
Step 8: Run the server and view the website

I have created two models - User and ActivityPeriod\
### User Model will store the user details
Model - User\
Table Name - user_details\
Fields - 3\
Fields Name - id, real_name, tz\

### ActivityPeriod Model will store the activities of each User
Model - ActivityPeriod\
Table Name - activity_periods\
Fields - 2\
Fields Name - start_time, end_time\

I have create two custom commands - createuser and createactivity
1. createuser will create 5 users with the User model
2. createactivity will create 3 activity periods for each user

API to view the JSON format of User and Activity Period - http://127.0.0.1:8000/user_activities/

Hosted in Heroku Apps - https://usersactivityperiod.herokuapp.com/





