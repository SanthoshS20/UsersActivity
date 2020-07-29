# Generated by Django 3.0.8 on 2020-07-29 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activity.User')),
            ],
            options={
                'db_table': 'activity_periods',
            },
        ),
    ]