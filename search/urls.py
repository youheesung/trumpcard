from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('result/', views.result, name='result'),
    path('', views.search, name='search'),
    path('detail/<str:playid>/', views.detail, name='detail'),
    path('review/<int:pk>/', views.review, name='review'),
    path('review/<str:playid>/', views.review, name='review'),
    path('review_create/<str:playid>/', views.review_create, name="review_create"),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),

    path('play_create/<str:username>/', views.play_create, name='play_create'),

    path('<str:playid>/like', views.to_my_heart, name='to_my_heart'),

    path('recommend/', views.recommend, name='recommend'),
    path('review/update/<int:pk>/', views.review_update, name='review_update')
]
