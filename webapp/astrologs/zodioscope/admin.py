from django.contrib import admin
from .models import ZodioscopeDaily

# Register your models here.

class ZodioscopeDailyAdmin(ZodioscopeDaily):
    list_display = ('current_date', 'sign')

admin.site.register(ZodioscopeDailyAdmin)
