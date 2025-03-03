from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models


# Create your views here.

def index(req):
    courses = models.Course.objects.all()

    return render(req, "shop/courses.html", {'courses': courses})

def single_course(req, course_id):
    # try:
    #     course = models.Course.objects.get(pk=course_id)
    #     return render(req, 'single_course.html', {'course': course})
    # except models.Course.DoesNotExist:
    #   raise Http404
    course = get_object_or_404(models.Course, pk=course_id)
    return render(req, 'shop/single_course.html', {'course': course})
    