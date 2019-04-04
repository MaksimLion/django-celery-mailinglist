from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = 'login.html'


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm 
    success_url = reverse_lazy('mailinglist:mailinglist_list')
