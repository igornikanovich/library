from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('user/<pk>',
         views.UserDetailView.as_view(), name='user-detail'),
    path('user/create/', views.UserCreateView.as_view(), name='user-create'),
    path('book/<pk>', views.BookUpdateView.as_view(), name='book-detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book-create'),
]
