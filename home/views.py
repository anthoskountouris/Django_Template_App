

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# decorator to block access to the page if the user is not logged in
# from django.contrib.auth.decorators import login_required

# class based views
# we can use to block access to the page if the user is not logged in
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import TemplateView  # class based views for templates
# class based views for login and logout pages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

from notes.models import Notes

# the below functions are replaced by the class based view

# def home(request):
#     # return HttpResponse("Hello World")
#     # original request, name of template, and brackets for context
#     return render(request, 'home/welcome.html', {'today': datetime.now().date(), 'name': 'Anthos'})

# Blocking the access to the page if the user is not logged in
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
    extra_context = {'today': datetime.now().date()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
    # extra_context = {}
