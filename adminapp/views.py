import string
import random
import datetime
import calendar
import time
from datetime import timedelta
from django.shortcuts import render,redirect,get_object_or_404
from.models import Task
from.forms import TaskForm
from django.contrib.auth import login as auth_login, authenticate
def Project(request):
    return render(request,'adminapp/Project.html' )

def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpagelogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'user input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)
def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')
from django.shortcuts import render

from django.http import HttpResponse
def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')
def randompagecall(request):
    return render(request,'adminapp/randomexm.html')
def randomlogic(request):
    if request.method=="POST":
        number1 = int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
    a1={'ran':ran}
    return render(request,'adminapp/randomexm.html',a1)
def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})
def calculatorpagecall(request):
    return render(request,'adminapp/calculator.html')
def daytimepagecall(request):
    return render(request,'adminapp/daytime.html')
def daytimepagelogic(request):
    if request.method=="POST":
        number1=int(request.POST['date1'])
        x=datetime.datetime.now()
        e=x+ timedelta(days=number1)
        e1=e.year
        e2=calendar.isleap(e1)
        if e2==False:
            e3="not a leap year"
        else:
            e3="leapyear"
    a1={'e':e,'e3':e3,'e1':e1,'number1':number1}
    return render(request,'adminapp/daytime.html',a1)
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
    tasks=Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form':form,'tasks':tasks})
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm-password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=firstname,
                    last_name=lastname,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Project.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')
def UserLoginPageCall(request):
    return render(request, 'adminapp/loginpage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'studentapp/StudentHomePage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomePage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('Project')
from .forms import StudentForm
from .models import StudentList
'''
from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})
'''
from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})

from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def upload_file(request):
    if request .method=='POST' and request.FILES['file']:
        file=request.FILES['file']
        df=pd.read_csv(file,parse_dates=['Date'],dayfirst=True)
        total_sales=df['Sales'].sum()
        average_sales=df['Sales'].mean()
        df['Month']=df['Date'].dt.month
        monthly_sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
        plt.pie(monthly_sales,labels=monthly_sales.index,autopct='%1.1f%%')
        plt.title('Sales distribution per month ')
        buffer=BytesIO()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_data=base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request,'adminapp/chart.html',{
            'total_sales':total_sales,
            'average_sales':average_sales,
            'chart':image_data
        })
    return render(request,'adminapp/chart.html',{'form':UploadFileForm})


from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'adminapp/feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'adminapp/feedback_success.html')


from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm
from django.conf import settings

def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})

def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Optional email functionality
            email_to = request.POST.get('email_to')
            if email_to:
                send_mail(
                    'New Contact Added',
                    f"Contact Details:\nName: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nAddress: {contact.address}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email_to],
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/contact_add.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'adminapp/contact_confirm_delete.html', {'contact': contact})