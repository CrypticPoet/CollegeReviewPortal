from django.contrib import admin
from django.db.models import Count

from .models import Professor, Course, Prof_review, Course_review

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'overall_rating')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'overall_rating')

class ProfReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'prof','report_count',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _report_count=Count("reports", distinct=True),
        )
        return queryset

    def report_count(self, obj):
        return obj._report_count
    report_count.admin_order_field = '_report_count'
    report_count.short_description = 'Reports'

class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'course', 'report_count')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _report_count=Count("creports", distinct=True),
        )
        return queryset

    def report_count(self, obj):
        return obj._report_count
    report_count.admin_order_field = '_report_count'
    report_count.short_description = 'Reports'


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Prof_review, ProfReviewAdmin)
admin.site.register(Course_review, CourseReviewAdmin)
