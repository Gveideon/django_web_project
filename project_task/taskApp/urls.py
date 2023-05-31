from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('list', views.listTask),
   path('add', views.addTask),
   path('editForm/<int:task_id>', views.editForm),
   path('<int:id_task>/', views.task, name="task"),
   path('deleteTask/<int:task_id>', views.delete)
]