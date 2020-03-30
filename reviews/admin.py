from django.contrib import admin
from .models import Professor, Course, Prof_review, Course_review

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'overall_rating')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'overall_rating')

class ProfReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__','total_reports',)

class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__','total_reports',)


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Prof_review, ProfReviewAdmin)
admin.site.register(Course_review, CourseReviewAdmin)
