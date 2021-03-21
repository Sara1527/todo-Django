from django.contrib import admin
from .models import TODO
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'title',
                    'priority',
                    'status',
                    'description']

admin.site.register(TODO,TodoAdmin)

