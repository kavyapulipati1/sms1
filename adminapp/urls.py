from django.urls import path,include
from.import views
from django import forms
urlpatterns=[
    path('',views.Project,name='Project'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randampagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('daytimepagecall/',views.daytimepagecall,name='daytimepagecall'),
    path('daytimepagelogic/', views.daytimepagelogic, name='daytimepagelogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),

    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.contact_add, name='contact_add'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),

]

