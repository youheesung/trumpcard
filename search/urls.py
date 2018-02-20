from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('result/', views.result, name='result'),
    path('', views.search, name='search'),
    path('<str:playid>/', views.detail, name='detail'),
    path('review/<int:pk>/', views.review, name='review'),
    path('review/<str:playid>/', views.review, name='review'),
    path('review_create/<str:playid>/', views.review_create, name="review_create"),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('<str:playid>/like', views.to_my_heart, name='to_my_heart'),

]
