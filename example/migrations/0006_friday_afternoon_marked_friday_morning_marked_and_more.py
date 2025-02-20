# Generated by Django 5.1.2 on 2025-02-09 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_alter_friday_user_alter_monday_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='friday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='friday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saturday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saturday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sunday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sunday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thursday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thursday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuesday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuesday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wednesday',
            name='afternoon_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wednesday',
            name='morning_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='friday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='friday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='monday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='monday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='cont',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
