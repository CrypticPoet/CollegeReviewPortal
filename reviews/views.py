from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Professor, Course, Prof_review, Course_review

def home(request) :
    return render(request, 'reviews/home.html')

class ProfessorListView(ListView):
    model = Professor
    template_name = 'reviews/profs.html'
    context_object_name = 'professors'

class ProfessorDetailView(DetailView):
    model = Professor

class CourseListView(ListView):
    model = Course
    template_name = 'reviews/courses.html'
    context_object_name = 'courses'
    ordering = ['code']

class CourseDetailView(DetailView):
    model = Course

class CourseReviewCreateView(LoginRequiredMixin, CreateView):
    model = Course_review
    fields = ['rating', 'body', 'anonymous']
    template_name = 'reviews/add_review.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = Course.objects.filter(pk=self.kwargs['pk']).first()
        return super().form_valid(form)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Prof_review
    fields = ['rating', 'body', 'anonymous']
    template_name = 'reviews/add_review.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.prof = Professor.objects.filter(pk=self.kwargs['pk']).first()
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Prof_review
    fields = ['rating', 'body', 'anonymous']
    template_name = 'reviews/add_review.html'

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Prof_review
    template_name = 'reviews/delete.html'

    def get_success_url(self):
        return reverse_lazy('prof-detail', kwargs={'pk':self.object.prof.id})

@login_required()
def report_review(request):
    review = get_object_or_404(Prof_review, pk=request.POST.get('review_id'))
    if request.method == 'POST':
        if review.reports.filter(id = request.user.id).exists() :
            messages.success(request, f'You have already made a report on this review')
            return redirect('prof-detail', pk=review.prof.pk)
        else:
            review.reports.add(request.user)
            messages.success(request, f'Review Reported Successfully')
            return redirect('prof-detail', pk=review.prof.pk)
    else:
        return redirect('prof-detail', pk=review.prof.pk)

class CourseReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Course_review
    fields = ['rating', 'body', 'anonymous']
    template_name = 'reviews/add_review.html'

class CourseReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Course_review
    template_name = 'reviews/delete.html'

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk':self.object.course.id})

@login_required()
def report_course_review(request):
    review = get_object_or_404(Course_review, pk=request.POST.get('review_id'))
    if request.method == 'POST':
        if review.creports.filter(id = request.user.id).exists() :
            messages.success(request, f'You have already made a report on this review')
            return redirect('course-detail', pk=review.course.pk)
        else:
            review.creports.add(request.user)
            messages.success(request, f'Review Reported Successfully')
            return redirect('course-detail', pk=review.course.pk)
    else:
        return redirect('course-detail', pk=review.course.pk)
