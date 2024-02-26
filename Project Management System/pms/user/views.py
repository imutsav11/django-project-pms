from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import ManagerCreationForm,DeveloperCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.views.generic import ListView
from django.urls import reverse

# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerCreationForm
    template_name = 'user/manager_register.html'
    success_url = '/login/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            


class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperCreationForm
    template_name = 'user/developer_register.html'
    success_url = '/login/'    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            
    
    
class UserLoginView(LoginView):  
    template_name = 'user/login.html'   
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/manager/'
            else:
                return '/developer/'

def sendMail(to):
    subject = 'Welcome to PMS'
    message = 'Hope you are enjoying your Django Tutorials'

    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    
    return True

class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager-dashboard/'
            else:
                return '/user/developer-dashboard/'
class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/manager_dashboard.html')
    
    
    template_name = 'user/manager_dashboard.html'

class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/developer_dashboard.html')
    
    template_name = 'user/developer_dashboard.html' 