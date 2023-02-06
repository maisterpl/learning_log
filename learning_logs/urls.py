from django.urls import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    # main site
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # web with courent topic and show details
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # web to add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # the web to add new entry to topic
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # path to edit_entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]