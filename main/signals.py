import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from main import models

logger=logging.getLogger()
@receiver(pre_save, sender=models.Talks)
def send_mail(sender, instance, **kwargs):
    if instance.pk != None:
        subject = 'Talk registered'
        message= 'Your proposal for  talk has been successfully registered.We will soon reviw it'
        from_email = 'admin@eventx.com'
        recipient_list = [instance.email, ]
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            logger.info(f'email successfully sent to {recipient_list}')
        
        except Exception as e:
            logger.error(f'failed to send email to {recipient_list} due to {e}')
            
            
        
    
