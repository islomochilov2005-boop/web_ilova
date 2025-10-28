from django.contrib import admin
from .models import News, Category, Contact


# admin.site.register(Category)
# admin.site.register(News)

@admin.register(Category)
class CaregoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'category']
    list_filter = ['title', 'status']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
