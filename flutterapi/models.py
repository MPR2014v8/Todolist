from django.db import models

class Todolist(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True) # ให้ detail ว่างได้

    def __str__(self):
        return self.title 