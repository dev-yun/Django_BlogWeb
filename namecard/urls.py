from django.urls import path

from namecard import views
from namecard.views import NamecardLV, NamecardDV

app_name = 'namecard'

urlpatterns = [
    path('', NamecardLV.as_view(), name='index'),
    path('namecard/', NamecardLV.as_view(), name='list'),
    path('namecard/<int:pk>/', NamecardDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='namecard_search'),
]