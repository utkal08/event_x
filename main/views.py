from django.shortcuts import render
from main import forms
from django.views.generic import FormView
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.TalksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '<h1>You have successfully registered your talk. The mail for approval will be sent shortly</h1>'
                )
    else:
        form=forms.TalksForm()
    return render(request, 'main/index.html', {'form':form})


def about(request):
    return render(request, 'main/about_us.html', {})


class ContactUsView(FormView):
    template_name="main/contact_form.html"
    form_class=forms.ContactForm
    success_url="/"

    def form_valid(self,form):
        form.send_mail()
        return super().form_valid(form)
