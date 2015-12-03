from django.shortcuts import render, redirect
# from django.http import HttpResponse
from todo.models import Item, List

# Create your views here.
def home_page(request):
#    return HttpResponse('<html><title>Welcome to Django. This is my cool Site!</title></html>')
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def view_todo(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'todo.html', {'list':list_})

def new_todo(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/todo/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/todo/%d/' % (list_.id,))
