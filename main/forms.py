from django import forms
from django.forms.widgets import Textarea
from django.core.mail import send_mail
from main import models
import logging

logger=logging.getLogger(__name__)


class ContactForm(forms.Form):
    name=forms.CharField(label='Your name',max_length=100,)
    message=forms.CharField(max_length=600,widget=Textarea)

    def send_mail(self):
        logger.info("Sending mail to customer service")
        message="From {0}\n{1}".format(
            self.cleaned_data["name"],
            self.cleaned_data["message"]
        )
        send_mail(
                "Site Message",
                message,
                "site@book_worms.domain",
                ["customerservice@book_worms.domain"],
                fail_silently=False
            )


class TalksForm(forms.ModelForm):
    class Meta:
        model = models.Talks
        fields = '__all__'
        exclude=['approved',]

