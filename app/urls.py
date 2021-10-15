from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('view',views.see,name='display'),
    path('form_submissionat',views.form_submissionat,name='success'),
    path('back',views.back,name='back'),
    path('print',views.print,name='print'),
]
