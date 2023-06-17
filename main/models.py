from django.db import models

# Create your models here.
class Talks(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    speaker = models.CharField(max_length=40)
    linkedin_profile = models.URLField()
    github_profile = models.URLField()
    approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.speaker
