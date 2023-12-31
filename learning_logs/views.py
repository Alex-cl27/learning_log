from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def get_index(request):
    """ Домашняя страница приложения learning log """
    return render(request, 'learning_logs/index.html')


@login_required
def get_topics(request):
    """ Выводит список тем """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def get_topic(request, topic_id):
    """ Выводит одну тему и все ее записи. """
    topic = Topic.objects.get(id=topic_id)
    # Проверка владельца темы (owner)
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def add_topic(request):
    """ Добавляет новую тему """
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'learning_logs/add_topic.html', context)


@login_required
def add_entry(request, topic_id):
    """ Добавляет новую запись по конкретной теме. """
    topic = Topic.objects.get(id=topic_id)
    # Проверка владельца темы (owner)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Вывести пустую или недействительную форму.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/add_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """ Редактирует существующую запись """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Проверка владельца темы (owner)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request, topic):
    """ Проверка владельца темы (owner) """
    if topic.owner != request.user:
        raise Http404
