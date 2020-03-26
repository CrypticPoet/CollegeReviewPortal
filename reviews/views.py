from django.shortcuts import render
from .models import Professor, Course
from django.http import HttpResponse

# professors = [{'name':'Prof. Ajit Kumar', 'department':'Applied Mechanics', 'courses':'APL100'},
#               {'name':'Prof. Subhasish Bannerjee', 'department':'Computer Science', 'courses':'COL100'},
#               {'name':'Prof. Bhim Singh', 'department':'Electrical Engineering', 'courses':'ELL100'}
#              ]

def home(request) :
    return render(request, 'reviews/home.html')

def prof_home(request) :
    context = {'professors':Professor.objects.all(), 'title':'Professors'}
    return render(request, 'reviews/profs.html', context)

def course_home(request) :
    context = {'courses':Course.objects.all(), 'title':'Courses'}
    return render(request, 'reviews/courses/html', context)