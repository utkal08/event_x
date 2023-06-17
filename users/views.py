from django.http import HttpResponse
from django.shortcuts import render,redirect
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from users import forms
from users.authentication import EmailAuthBackend
# Create your views here.
logger = logging.getLogger(__name__)


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.UserCreationForm
    
    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self,form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get('email')
        logger.info(
            "New signup for email=%s through SignUpView".format(email)
        )
        form.send_mail()
        messages.info(
            self.request,'You signed up successfully'
        )
        return response


def login(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user=EmailAuthBackend.authenticate(request,email,password,backend='users.authentication.EmailAuthBackend')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('User is not active')
    else:
        form = forms.AuthenticationForm()
        
    return render(request,'users/login.html',{'form':form})
        
        

    
