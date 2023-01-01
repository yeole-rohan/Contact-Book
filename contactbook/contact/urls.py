
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import loginView, index, registration, create, contactBookDetail, search

urlpatterns = [
    path("login/", loginView, name="loginView"),
    path("", index, name="index"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("registration/", registration, name="registration"),
    path("create/", create, name="create"),
    path("deatils/<int:pk>/", contactBookDetail, name="contactBookDetail"),
    path("search/<str:search_term>/", search, name="search"),
]
