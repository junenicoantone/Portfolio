from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

class Skill(models.Model):
    name = models.CharField(max_length=50)