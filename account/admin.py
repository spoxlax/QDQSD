from django.contrib import admin
from .models import Account


# from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin')


admin.site.register(Account, AccountAdmin)
