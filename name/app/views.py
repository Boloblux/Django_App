from multiprocessing import context
import re
from django.shortcuts import get_object_or_404, render
 
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .forms import BuyForm, QuestionForm
from django.utils import timezone

def index(request):

    return render(request, 'app/index.html')

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Question.objects.all()

    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
         
    return render(request, "app/list_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)
         
    return render(request, "app/detail_view.html", context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "app/update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/app/list")
 
    return render(request, "app/delete_view.html", context)

def buy_view(request, id):
    context ={}

    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)

    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
    stock = obj.quantity
 
    # pass the object as instance in form
    form = BuyForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        quantity_buy = obj.quantity
        stock_rest = stock - quantity_buy
        obj.quantity = stock_rest
        form.save()
        return HttpResponseRedirect("/app/"+id)
 
    # add form dictionary to context
    context["form"] = form
         
    return render(request, "app/buy_view.html", context)

def chat_index(request):

    return render(request, 'app/chat_index.html')

def chat_room(request, room_name):
    return render(request, 'app/chat_room.html', {
        'room_name': room_name
    })