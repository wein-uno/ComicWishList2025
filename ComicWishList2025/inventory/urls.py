from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_comic, name='add_comic'),
    path('list/', views.comic_list, name='comic_list'),  # New URL for comic list
    path('comic/<int:comic_id>/image/', views.view_comic_image, name='view_comic_image'),

]
