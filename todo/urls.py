from django.urls import path

from todo.api.views import LoginView, RegistrationView

urlpatterns = [
    #auth
    path("registration/", RegistrationView.as_view()),
    path("login/", LoginView.as_view()),
]
