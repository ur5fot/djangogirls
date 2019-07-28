from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from blog.views import PostsViewSet
from . import views

router = DefaultRouter()
router.register('api/post', PostsViewSet, basename='api_post')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', include(router.urls))
]
