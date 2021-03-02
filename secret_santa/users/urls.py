from django.urls import path

from .views import CustomLoginView, log_out, register, profile, edit_profile

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('me/', profile, name='profile'),
    path('me/edit/', edit_profile, name='edit_profile'),

]
