from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from users.forms import UserRegistrationForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    extra_context = {
        "next": reverse_lazy('landing_page')
    }


def log_out(request):
    logout(request)
    return redirect(reverse('login'))

def profile(request):

    return render(request, template_name='users/profile.html')


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'users/register.html', context={"form": form})
    else:
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('login'))
        else:
            return redirect('register')

def edit_profile(request):
    return render(request, 'users/edit_profile.html')
