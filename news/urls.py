from django.urls import path
from .views import *
from news.auth.views import login

urlpatterns = [
    # sayt qism uchun 
    path("", index, name="index"),
    path("ctg/<slug>/", ctg, name="ctg"),
    path("cnt/ ", cnt, name="cnt"),
    path("view/<int:pk>", view, name="view"),
    path("search/", search, name="search"),

    # auth qism uchun
    path("login/", login, name="login")
]
