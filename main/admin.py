from django.contrib import admin
from main import models
# Register your models here.


class TalkAdmin(admin.ModelAdmin):
    list_display = (
        'title','description','speaker','linkedin_profile','github_profile','approved',
    )
    list_editable=('approved',)

admin.site.register(models.Talks,TalkAdmin)