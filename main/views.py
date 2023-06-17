from django.shortcuts import render
from main import forms
from django.views.generic import FormView
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})


def about(request):
    return render(request, 'main/about_us.html', {})


class ContactUsView(FormView):
    template_name="main/contact_form.html"
    form_class=forms.ContactForm
    success_url="/"

    def form_valid(self,form):
        form.send_mail()
        return super().form_valid(form)