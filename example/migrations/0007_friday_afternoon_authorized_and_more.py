# Generated by Django 5.1.2 on 2025-02-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_friday_afternoon_marked_friday_morning_marked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='friday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saturday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saturday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sunday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sunday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thursday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thursday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuesday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuesday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wednesday',
            name='afternoon_authorized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wednesday',
            name='morning_authorized',
            field=models.BooleanField(default=False),
        ),
    ]
