# Generated by Django 3.0.4 on 2020-04-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_employer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(blank=True, default='0.00', help_text='Default currency is INR ₹', max_length=15, null=True),
        ),
    ]