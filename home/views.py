from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/index.html', {})
def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
