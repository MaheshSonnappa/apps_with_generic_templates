from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse("<h1>This is app2 view</h1>")

def app2_html(request):
    return render(request, "app2.html")