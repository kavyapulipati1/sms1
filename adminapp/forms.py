import pytz
from django import forms
from.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()


from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone_number', 'feedback')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
