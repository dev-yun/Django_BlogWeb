from django.urls import path

from bookmark import views

app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('bookmark/', views.BookmarkLV.as_view(), name='list'),
    path('bookmark/<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='bookmark_search'),

    path("add/", views.BookmarkCreateView.as_view(), name="add"),
    path("change/", views.BookmarkChangeLV.as_view(), name="change"),
    path("<int:pk>/update/", views.BookmarkUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.BookmarkDeleteView.as_view(), name="delete"),
]