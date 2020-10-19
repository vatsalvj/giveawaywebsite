from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

urlpatterns=[
    path("",views.index,name="index"),

    path("pr/",views.pr,name="pr"),

    path('login/', auth_views.LoginView.as_view(template_name="login.html")),

    path('logout/', views.logout_view),
]