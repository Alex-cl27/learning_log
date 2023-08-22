from django.shortcuts import render
from .models import Topic


# Create your views here.
def get_index(request):
    """ Домашняя страница приложния learning log """
    return render(request, 'learning_logs/index.html')


def get_topics(request):
    """ Выводит список тем """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def get_topic(request, topic_id):
    """ Выводит одну тему и все ее записи. """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
