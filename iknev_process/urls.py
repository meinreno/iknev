from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from iknev_process import views

urlpatterns = [
    path('processes', views.processes, name='processes'),
    path('process/<int:pk>/', views.process, name='process_details'),
    path('process/', views.process, name='process_method'),

    path('actions/', views.actions, name='actions'),

    path('processesways/', views.processes_ways, name='processesways'),
]

urlpatterns = format_suffix_patterns(urlpatterns)