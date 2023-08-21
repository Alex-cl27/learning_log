from django.contrib import admin
from .models import Topic

# Управление моделью осуществляется через админку:
admin.site.register(Topic)
