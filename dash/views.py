from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

# Create your views here.
def index(request):
    context = {
        "orders": Item.objects.all()
    }
    return render(request, "dash/index.html", context)