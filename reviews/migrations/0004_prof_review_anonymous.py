# Generated by Django 3.0.4 on 2020-03-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_prof_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof_review',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]