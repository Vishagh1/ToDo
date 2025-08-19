from django.shortcuts import render
from task.models import Task

def home(request):
    t = Task.objects.filter(is_completed=False).order_by('updated_at')
    ct = Task.objects.filter(is_completed=True)
    context = {
        "tasks" : t,
        "ct" : ct,
    }
    return render(request,'home.html',context)