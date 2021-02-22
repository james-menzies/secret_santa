from django.urls import path

from .views import CustomLoginView, log_out, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register')
]
