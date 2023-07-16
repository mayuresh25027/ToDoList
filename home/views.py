from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from home.models import  todoTasks
from django.urls import reverse
# Create your views here.

def create(request):
    context = {'success':False}
    if request.method == "POST":
        # handeling the form 
        title = request.POST['title']
        desc = request.POST['desc']
        start = request.POST['startDateInput']
        end = request.POST['endDateInput']
        completed = request.POST.get('isCompleted', False) == "on"
        print(completed)
        ins = todoTasks(taskTitle = title, taskDescription = desc , startDate = start, endDate = end, isCompleted = completed)
        ins.save()
        context = {'success':True}
    return render(request, 'task.html',context)

def home(request):
    todoData = todoTasks.objects.all()
    context = {"todoTask":todoData}
    return render(request, 'index.html',context)

def delete(request, id):
  member = todoTasks.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('home'))


def edit(request, id):
    member = todoTasks.objects.get(id=id)
    mydict = {
        'title': member.taskTitle,
        'desc':member.taskDescription,
        'startDate': member.startDate,
        'endDate': member.endDate,
        'completed':member.isCompleted,
        'id':member.id
    }

    print(mydict)
    return render(request, 'edit.html', context=mydict)


def update(request, id):
    if request.method == "POST":
        # handeling the form 
        title = request.POST['title']
        desc = request.POST['desc']
        start = request.POST['startDateInput']
        end = request.POST['endDateInput']
        completed = request.POST.get('isCompleted', False) == "on"
        ins = todoTasks(id = id, taskTitle = title, taskDescription = desc ,  startDate = start, endDate = end, isCompleted = completed)
        ins.save()
    return HttpResponseRedirect(reverse('home'))