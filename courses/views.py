from django.shortcuts import render
from courses.models import Course
from django.http import HttpResponse

# Create your views here.
def course_list(request):
	c = Course()
	return c.title