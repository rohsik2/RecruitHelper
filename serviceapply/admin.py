from django.contrib import admin
from .models import Service, Cutline


class CutlineInline(admin.TabularInline):
    model = Cutline


class ServiceAdmin(admin.ModelAdmin):
    inlines = (CutlineInline,)


admin.site.register(Service, ServiceAdmin)
