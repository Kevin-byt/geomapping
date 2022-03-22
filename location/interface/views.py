import sys
from subprocess import run
from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404,redirect
# from django.http import HttpResponse
# Path(BASE_DIR,"..//geo.py")

# Create your views here.

def page_view(request):
    return render(request, "home.html")

def external(request):
    out= run([sys.executable,'D:\Account\Dropbox\Dev\Projects\python\Geolocation\env\src\geo.py'],shell=True)
    print("Hello")
    return render(request,"home.html")
    