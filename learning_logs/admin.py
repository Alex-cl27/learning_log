from django.contrib import admin
from .models import Topic, Entry

# Управление моделью осуществляется через админку:
admin.site.register(Topic)
admin.site.register(Entry)
