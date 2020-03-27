from django.contrib import admin
from .models import Professor, Course, Prof_review

admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Prof_review)
