from django.contrib import admin

from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']

    '''fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]'''
admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

    '''fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]'''

admin.site.register(Page, PageAdmin)
