from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/new/', views.group_new, name='create_group'),
    path('group/<int:pk>/edit/', views.group_edit, name='edit_group'),
    path("post/new/", views.new_post, name="create_post"),
    path("post/edit/<int:pk>/", views.edit_post, name="edit_post"),
]