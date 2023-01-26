from django.urls import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    # main site
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # web with courent topic and show details
    path('topics/<int:topic_id>/', views.topic, name='topic')
]