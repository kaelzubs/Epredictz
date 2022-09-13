# Generated by Django 4.1.1 on 2022-09-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_dat', models.CharField(max_length=100)),
                ('match_time', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('league', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('tip', models.CharField(max_length=100)),
                ('tip_odd', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
