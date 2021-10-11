from django.urls import path

from bookmark import views
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('bookmark/', BookmarkLV.as_view(), name='list'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='bookmark_search'),
]