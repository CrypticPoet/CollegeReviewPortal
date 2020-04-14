from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Professor(models.Model) :
    name = models.CharField(max_length=100)
    position = models.TextField(default='Assistant Professor')
    education = models.TextField()
    department = models.TextField()
    description = models.TextField(default='No Description yet')
    email = models.EmailField(default='mail@example.com')
    contact = models.CharField(max_length=20)
    image = models.ImageField(default='default_prof.jpg', upload_to='professor_pics')

    def overall_rating(self):
        sum = 0
        count = self.reviews.count()
        if count == 0:
            return
        else :
            for review in self.reviews.all() :
                sum += review.rating
        return f'{(sum/count):.1f}'
    overall_rating.short_description = 'Rating'

    def __str__(self):
        return self.name

class Course(models.Model) :
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    department = models.TextField()
    description = models.TextField(default='No Description yet')
    instructor = models.ManyToManyField(Professor)

    def overall_rating(self):
        sum=0
        count=self.course_reviews.count()
        if count == 0 :
            return
        else :
            for review in self.course_reviews.all() :
                sum += review.rating
        return f'{(sum/count):.1f}'
    overall_rating.short_description = 'Rating'

    def __str__(self):
        return self.name

class Prof_review(models.Model):
    rating_choices = [(x, f'{x}') for x in range(1, 11)]
    rating = models.PositiveSmallIntegerField(default=0, choices=rating_choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(editable=True)
    datetime = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False, blank=True)
    reports = models.ManyToManyField(User, blank=True, related_name='reports')
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reviews')

    def total_reports(self):
        return self.reports.count()
    total_reports.short_description = 'Reports'

    def get_absolute_url(self):
        return reverse('prof-detail', kwargs={'pk':self.prof.pk})

    class Meta:
        ordering = ['-datetime']
    def __str__(self):
        return f'{self.author.username} on {self.prof.name}'

class Course_review(models.Model):
    rating_choices = [(x, f'{x}') for x in range(1, 11)]
    rating = models.PositiveSmallIntegerField(default=0, choices=rating_choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(editable=True)
    datetime = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False, blank=True)
    creports = models.ManyToManyField(User, blank=True, related_name='creports')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_reviews')

    def total_reports(self):
        return self.creports.count()
    total_reports.short_description = 'Reports'

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk':self.course.pk})

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f'{self.author.username} on {self.course.name}'