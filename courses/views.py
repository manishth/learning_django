from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Course

# Create your views here.
def course_list(request):
	c = Course()
	return HttpResponse(c.title)