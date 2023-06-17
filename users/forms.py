from django.contrib.auth.forms import(
    UserCreationForm as DjangoUserCreationForm
)
import logging
from django.contrib.auth.forms import UsernameField
from users import models
from django.core.mail import send_mail
from django import forms


logger = logging.getLogger(__name__)

#signup form
class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {"email":UsernameField}
        
    def send_mail(self):
        logger.info(
            "Sending signup email for emails=%s",
            self.cleaned_data['email'],
        )

        message = "Welcome {}".format(self.cleaned_data['email'])
        send_mail(

            "Welcome to event_x",
            message,
            "site@event_x.com",
            [self.cleaned_data['email']],
            fail_silently=True
            )

# login form
class AuthenticationForm(forms.Form):
    username=forms.EmailField()
    password=forms.CharField(strip=False,widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'

        
