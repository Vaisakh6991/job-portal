# Generated by Django 3.0.4 on 2020-04-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_auto_20200408_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='working_time',
        ),
        migrations.AddField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('full time', 'Full time'), ('part time', 'Part time'), ('internship', 'Internship')], default='full time', max_length=50),
            preserve_default=False,
        ),
    ]