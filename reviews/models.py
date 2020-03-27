from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model) :
    name = models.CharField(max_length=100)
    position = models.TextField(default='Assistant Professor')
    education = models.TextField()
    department = models.TextField()
    description = models.TextField(default='No Description yet')
    email = models.EmailField(default='mail@example.com')
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model) :
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    department = models.TextField()
    instructor = models.ManyToManyField(Professor)

    def __str__(self):
        return self.name

class Prof_review(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(editable=True)
    datetime = models.DateTimeField(auto_now_add=True)
    reported = models.PositiveSmallIntegerField(default=0, name='Reports')

    class Meta:
        ordering = ['-datetime']
    def __str__(self):
        return f'{self.author.username} on {self.prof.name}'