from django.contrib import admin
from blog.models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)