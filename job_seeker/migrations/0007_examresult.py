# Generated by Django 3.0.4 on 2020-07-13 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0006_auto_20200713_1241'),
        ('job_seeker', '0006_auto_20200713_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examResult', to='job_seeker.JobSeeker')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examResult', to='employer.Jobs')),
            ],
        ),
    ]