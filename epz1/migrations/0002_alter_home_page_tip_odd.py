# Generated by Django 4.1.1 on 2023-02-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("epz1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home_page",
            name="tip_odd",
            field=models.FloatField(default=None),
        ),
    ]