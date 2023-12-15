from django.shortcuts import render, redirect
from django.http import HttpResponse
from .task import *
# Create your views here.
def home(request):
    export_student_excel.delay()
    return HttpResponse("Hello From Cellery")