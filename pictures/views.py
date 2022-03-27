from django.shortcuts import render
from django.http  import HttpResponse
from .models import Galore
import datetime as dt

# Create your views here.
def main(request):  

    # Function that gets the date
    date = dt.date.today()
    post = Galore.days_post()

    return render(request, 'main.html',{"date": date,"post":post})

