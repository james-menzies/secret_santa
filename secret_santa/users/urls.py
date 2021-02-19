from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.view_user, name="view_user"),
    path('login/', views.login, name="login")
]
