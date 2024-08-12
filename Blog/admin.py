from django.contrib import admin

from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url', 'add_date')
    search_fields = ('title', 'url', 'add_date')
    
    
class PostAdmin(admin.ModelAdmin):
    # list_display = ('image_tag', 'title', 'content', 'url', 'cat', 'image')
    list_display = ('image_tag', 'title')
    list_filter = ('cat',)
    list_per_page = 5
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)