from django.db import models

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
