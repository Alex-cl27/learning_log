""" Определяет схемы URL для learning_logs """

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.get_index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.get_topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.get_topic, name='topic'),
    # Страница для добавления новой темы
    path('topics/add_topic/', views.add_topic, name='add_topic'),
    # Страница для добавления новой записи
    path('topics/<int:topic_id>/add_entry/', views.add_entry, name='add_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]
