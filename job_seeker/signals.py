from django.db.models.signals import post_save
from django.dispatch import receiver

from employer.models import Employer, ExamQuestion, OpenedExams, Jobs
from job_seeker.models import User, JobSeeker, Resumes, Address



# create profile if the user is employee 

@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_employee:
            JobSeeker.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    if instance.is_employee:
        instance.jobseeker.save()


# create profile for employer

@receiver(post_save, sender=User)
def create_employer_profile(sender, instance, created, **kwargs):
    if created:
        if  not instance.is_employee:
            Employer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employer_profile(sender, instance, **kwargs):
    if not instance.is_employee:
        instance.employer.save()


# when a user is created a resume filed is created for the user 

@receiver(post_save, sender=JobSeeker)
def create_resume(sender, instance, created, **kwargs):
    if created:
        if instance.user.is_employee:
            Resumes.objects.create(jobseeker=instance)

@receiver(post_save, sender= JobSeeker)
def save_resume(sender, instance, **kwargs):
    if instance.user.is_employee:
        instance.resumes.save()


# when a user is created a address filed is created for the user 

@receiver(post_save, sender=JobSeeker)
def create_address(sender, instance, created, **kwargs):
    if created:
        if instance.user.is_employee:
            Address.objects.create(jobseeker=instance)

@receiver(post_save, sender= JobSeeker)
def save_address(sender, instance, **kwargs):
    if instance.user.is_employee:
        instance.address.save()


# Create status of exam in OpenedExams model when a Question is added to ExamQuestions model

@receiver(post_save, sender=Jobs)
def create_exam_status(sender, instance, created, **kwargs):
    if created: 
        OpenedExams.objects.create(job=instance)


@receiver(post_save, sender=Jobs)
def save_exam_status(sender, instance, **kwargs):
    if instance.is_opened == False: # if job is closed, exam is open
        instance.openedExams.update(is_open = True)
    if instance.is_opened:
        instance.openedExams.update(is_open = False)