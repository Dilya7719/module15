# Generated by Django 4.2.1 on 2023-07-13 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_subscribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
