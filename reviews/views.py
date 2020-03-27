from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Professor, Course


def home(request) :
    return render(request, 'reviews/home.html')

class ProfessorListView(ListView):
    model = Professor
    template_name = 'reviews/profs.html'
    context_object_name = 'professors'

class ProfessorDetailView(DetailView):
    model = Professor

@login_required()
def add_review(request, pk):
    prof = get_object_or_404(Professor, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.prof = prof
            review.author = request.user
            review.save()
            return redirect('prof-detail', pk=prof.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

class CourseListView(ListView):
    model = Course
    template_name = 'reviews/courses.html'
    context_object_name = 'courses'
    ordering = ['code']

class CourseDetailView(DetailView):
    model = Course