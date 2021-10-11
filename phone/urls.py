from django.urls import path

from phone import views
from phone.views import PhoneLV, PhoneDV

app_name = 'phone'

urlpatterns = [
    path('', PhoneLV.as_view(), name='index'),
    path('phone/', PhoneLV.as_view(), name='list'),
    path('phone/<int:pk>', PhoneDV.as_view(), name='number'),
    path('search/', views.SearchFormView.as_view(), name='phone_search'),
]

