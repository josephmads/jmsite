from django.contrib import admin
from blog.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published')

class PageElementAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(PageElement, PageElementAdmin)