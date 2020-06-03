from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_toDo/', views.add_toDo, name = 'add_toDo'),
    path('delete_toDo/<int:toDo_id>/', views.delete_toDo, name = 'delete_toDo'),
    path('<int:toDo_id>/details/', views.details_toDo, name = 'details_toDo'),
]