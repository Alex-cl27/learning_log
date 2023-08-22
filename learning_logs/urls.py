""" Определяет схемы URL для learning_logs """

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.get_index, name='index'),
    # Страницв со списком всех тем.
    path('topics/', views.get_topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.get_topic, name='topic'),
    # Страница для добавления новой темы
    path('add_topic/', views.add_topic, name='add_topic'),
    # Страница для добавления новой записи
    path('add_entry/<int:topic_id>', views.add_entry, name='add_entry'),
]
