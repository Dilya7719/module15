from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_create_date', 'post_header'] # генерируем список имён всех полей для более красивого отображения
    list_filter = ['post_create_date', 'post_header']
    search_fields = ['post_header']




admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
