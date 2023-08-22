from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


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


def add_topic(request):
    """ Добавляет новую тему """
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправленны данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'learning_logs/add_topic.html', context)
