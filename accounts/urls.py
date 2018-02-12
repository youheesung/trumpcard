from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('signup/', views.signup, name='signup'),
]
