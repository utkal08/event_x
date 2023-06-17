from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from users import models
# Register your models here.
@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields":("email", "password")}),
        ("Personal info", {"fields":("first_name", "last_name")}),
        ("Permissions", {"fields":('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ("Impoertant dates", {"fields":('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
        None,
        {
            'classes':('wide',),
            'fields':('email','password1','password2'),
        }),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering=('email',)
