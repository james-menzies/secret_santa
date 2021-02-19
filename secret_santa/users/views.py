from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from users.models import CustomUser


def login(request):
    return render(request, 'users/login.html')

def view_user(request, id):
    user = CustomUser.objects.get(pk=id)
    context = {
        "user": user,
    }
    return render(request, 'users/view_user.html', context=context)
