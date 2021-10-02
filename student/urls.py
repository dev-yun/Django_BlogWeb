from django.urls import path

from student import views
from student.views import StudentLV, StudentDV

app_name = 'student'

urlpatterns = [
    path('', StudentLV.as_view(), name='index'),
    path('student/', StudentLV.as_view(), name='list'),
    path('student/<int:pk>/', StudentDV.as_view(), name='detail'),
]