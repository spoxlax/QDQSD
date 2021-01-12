from django.contrib import admin
from .models import Ticket, Status, Priority, Category

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Category)
