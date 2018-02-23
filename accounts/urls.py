from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('signup/', views.signup, name='signup'),
    path('profile_update/<str:username>/', views.profile_update, name="profile_update"),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommend_2/', views.recommend_2, name="recommend_2"),
]
