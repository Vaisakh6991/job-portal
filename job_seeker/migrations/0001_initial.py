# Generated by Django 3.0.4 on 2020-04-10 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'required': 'Please provide email', 'unique': 'This email address is taken'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(error_messages={'required': 'Please provide phone number', 'unique': 'This phone number is taken'}, max_length=15, null=True, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('is_employee', models.BooleanField(default=True)),
                ('account_confirmed', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resumes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
                ('jobseeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='job_seeker.JobSeeker')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('jobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobapplication', to='employer.Jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobapplication', to='job_seeker.JobSeeker')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(blank=True, help_text='House/Buiding Name', max_length=50, null=True)),
                ('street', models.CharField(blank=True, help_text='Road/Area', max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('land_mark', models.CharField(blank=True, max_length=100, null=True)),
                ('jobseeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='job_seeker.JobSeeker')),
            ],
        ),
    ]
