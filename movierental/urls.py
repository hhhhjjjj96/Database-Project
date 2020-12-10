from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_page/', views.user_page, name='user_page'),
    path('edit_user_info/', views.edit_user_info, name='edit_user_info'),
    path('movies/', views.get_bestseller, name='movies'),
    path('moviequeue/', views.get_moviequeue, name='moviequeue'),
    path('add_moviequeue/', views.add_moviequeue, name='add_moviequeue'),
    path('search/', views.search, name='search'),
    path('order_page/', views.order_page, name='order_page'),
    path('order/', views.order, name='order'),
    path('return_order/', views.return_order, name='return_order'),
    path('rating/', views.return_order, name='rating'), 
    path('signup/', views.signup, name='signup'),
    path('genre/', views.genre, name='genre'),
]
