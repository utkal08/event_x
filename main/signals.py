import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from main import models
from django.core.mail import send_mail


logger=logging.getLogger(__name__)
@receiver(post_save, sender=models.Talks)
def send_registration_mail(sender, instance, **kwargs):
        subject = 'Talk registered'
        message= 'Your proposal for  talk has been successfully registered.We will soon reviw it'
        from_email = 'admin@eventx.com'
        recipient_list = [instance.email, ]
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)
        logger.info('email successfully sent to {}'.format(recipient_list))
        
            
@receiver(post_save,sender=models.Talks)
def send_approved_mail(sender,instance,**kwargs):
    if instance.approved=="True":
        subject="Talk approved"
        message=f"Congratulations, your talk{instance.title} has been approved"
        from_email='admin@eventx.com'
        recipient_list=[instance.email,]    
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        logger.info('Successfully sent the mail to {}'.format(recipient_list))