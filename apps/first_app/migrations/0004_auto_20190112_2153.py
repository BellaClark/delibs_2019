# Generated by Django 2.0.7 on 2019-01-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20190112_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='people_voted',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='person',
            name='total_vote',
            field=models.IntegerField(default='0'),
        ),
    ]
