from django.contrib import admin

# Register your models here.
from .models import Task

# Zaregistrovanie Tasku (cast model) pre admina
admin.site.register(Task)