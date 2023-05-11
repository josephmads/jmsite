from django.contrib import admin
from base.models import PageElement


# Register your models here.

class PageElementAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(PageElement, PageElementAdmin)