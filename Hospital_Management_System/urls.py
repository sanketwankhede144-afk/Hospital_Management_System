from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Index, name='home'),
    path('about/', About, name='about'),
    path('admin_login/', Login, name='login'),
    path('contact/', Contact, name='contact'),
    path('logout/', Logout_admin, name='logout'),

    path('view_doctor/', View_doctor, name='view_doctor'),
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('delete_doctor/<int:pid>/', Delete_Doctor, name='delete_doctor'),

    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_patient/<int:pid>/', Delete_Patient, name='delete_patient'),

    path('view_appointement/', View_Appointement, name='view_appointment'),
    path('add_appoointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointent/<int:pid>/', Delete_Appointment, name='delete_appointement'),
]