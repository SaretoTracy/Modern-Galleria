from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def main(request):  

    # Function that gets the date
    date = dt.date.today()

    return render(request, 'main.html',{"date": date})