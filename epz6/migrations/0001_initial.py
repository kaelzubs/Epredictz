# Generated by Django 4.1.1 on 2022-09-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cookie_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('bodytext', models.TextField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
