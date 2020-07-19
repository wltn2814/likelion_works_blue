from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/',views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('create/',views.create, name='create'),
    path('<int:blog_id>/delete/', views.delete, name = 'delete'),
    path('<int:blog_id>/delete_r/', views.delete_r, name = 'delete_r'),
    path('<int:blog_id>/update', views.update, name = 'update'),
    path('<int:blog_id>/update_r/', views.update_r, name = 'update_r'),
    path('revise/', views.revise, name = 'revise'),
]