from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from taskApp.models import Task

def index(request):
   return render(request, "index.html")
def listTask(request):
   tasks = Task.objects.all()
   context = {
      "taskList" : tasks
   }
   return render(request, "task_list.html", context)
   #return HttpResponse(f"<h2>Список дел</h2> {tasks[0]}")
def addTask(request):
   message = ""
   if request.method == "POST":
      task = request.POST.get("task", "ничего!")
      newtask = Task.objects.create(task=task)
      if str(task) != "ничего!":
         message = "add new task" + str(task)
         context = {
            "message" : message
         }
      print(task)
   context = {
         "message" : message
      }
   return render(request, "addTask.html", context)


def task(request, id_task):
   task = Task.objects.all()[id_task]
   return HttpResponse(f"<h2>Список дел</h2> {task}")
def delete(request, task_id):
   try:
      _task = Task.objects.get(id = task_id)
      # Tasks.objects.filter(id=task_id).delete()
      _task.delete()
      return HttpResponseRedirect("../list")
   except:
      return HttpResponseNotFound()

def editForm(request, task_id):
   if request.method == "POST":
      text = request.POST.get("task", "ничего!")
      _task = Task.objects.get(id = task_id)
      if str(task) != "ничего!":
         try:
          # Tasks.objects.filter(id=task_id).delete()
            _task.task = text
            _task.update()
            return HttpResponseRedirect("../list")
         except:
            return HttpResponseNotFound()
   else:
      context = {
      "task_id" : task_id
      }
      return render(request, "editTask.html", context)