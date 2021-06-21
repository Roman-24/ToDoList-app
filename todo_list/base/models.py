from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# zadefinovanie modelu -> Task
class Task(models.Model):
    
    # on_delete je co ak user neexistuje 
    # to CASCADE je ze vsetky child objekty
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["complete"]