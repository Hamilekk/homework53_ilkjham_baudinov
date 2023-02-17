from django.urls import path

from webapp.views.task import add_view, detail_view, edit_task
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', add_view, name='task_add'),
    path('task/<int:pk>/', detail_view, name='task_detail'),
    path('task/edit/<int:pk>/', edit_task, name='task_edit'),
]
