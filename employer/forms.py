from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from job_seeker.models import User
from employer.models import Jobs, Employer, ExamQuestion

class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','phone']
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.is_employee = False
        if commit:
            user.save()
        return user


class PostJobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'description','qualifications','experience', 'salary', 'location', 'type', 'is_opened']

class ProfileUpadteForm(ModelForm):
    class Meta:
        model = Employer
        fields = ['location', 'address']

class ExamCreateForm(ModelForm):
    class Meta:
        model = ExamQuestion
        fields =  ['question', 'option1','option2','option3', 'answer']