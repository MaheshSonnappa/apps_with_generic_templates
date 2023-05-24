from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse("<h1>This is app1_string view</h1>")

def app1_html(request):
    return render(request, "app1.html")

