from django.http import HttpResponse
from django.shortcuts import render

from .models import Course

# Create your views here.
def course_list(request):
	c = Course.objects.all()
	output = ', '.join([str(courseList) for courseList in c])
	return HttpResponse(output)