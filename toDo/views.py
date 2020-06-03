from django.shortcuts import render
from django.utils import timezone
from .models import toDo
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import toDoForm
# Create your views here.
def home(request):
    todo_items = toDo.objects.all().order_by("-added_date")
    #print(todo_items)
    context ={
        'todo_items': todo_items,
    }
    return render(request, 'toDo/index.html', context)

def add_toDo(request):
    text = request.POST.get('content')
    if text != "":
        toDo.objects.create(text = text, added_date = timezone.now())
    return HttpResponseRedirect('/')

def delete_toDo(request, toDo_id):
    toDo.objects.get(id= toDo_id).delete()
    return HttpResponseRedirect('/')

def details_toDo(request, toDo_id):
    initial_data = toDo.objects.get(id= toDo_id)
    data = {'Todo':initial_data.text, 'Date': initial_data.added_date, 'Description':initial_data.description}
    print(data)
    my_form = toDoForm(data)
    if request.POST:
        initial_data.description = request.POST.get('Description')
        initial_data.save()
        print(initial_data)
        data['Description'] = initial_data.description
        my_form = toDoForm(data)
        if my_form.is_valid():
            print(my_form.cleaned_data)
    context = {
        'form':my_form,
    }
    return render(request, 'toDo/details.html', context)
    