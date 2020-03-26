from django.shortcuts import render
from .models import Professor, Course
from django.http import HttpResponse

def home(request) :
    return render(request, 'reviews/home.html')

def prof_home(request) :
    context = {'professors':Professor.objects.all(), 'title':'Professors'}
    return render(request, 'reviews/profs.html', context)

def course_home(request) :
    context = {'courses':Course.objects.all(), 'title':'Courses'}
    return render(request, 'reviews/courses.html', context)