from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall, name='wall'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('suggestions/', views.suggestions, name='suggestions'),
]
