# Generated by Django 3.0.4 on 2020-07-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0005_jobs_job_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_expiry',
            field=models.BooleanField(default=True),
        ),
    ]
