from django.contrib import admin

# Register your models here.
from .models import Service, Cutline


admin.site.register(Service)
admin.site.register(Cutline)
