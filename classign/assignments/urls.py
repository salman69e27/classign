from django.urls import path
from . import views

app_name = 'assignments'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<str:lms_name>/<int:assignment_id>', views.assignment, name='assignment'),
    path('submit/<int:assignment_id>', views.assignment, name='assignment')
]
