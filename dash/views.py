from django.http import HttpResponse
from django.shortcuts import render

from .models import Task

# Create your views here.
def index(request):
    context = {
        "orders": Task.objects.all()
    }
    return render(request, "dash/index.html", context)