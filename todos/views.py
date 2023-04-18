from django.shortcuts import render
from todos.models import TodoList


def todo_list_list(request):
    lists = TodoList.objects.all()
    context = {
        "lists": lists,
    }
    return render(request, "todo_lists/list.html", context)
