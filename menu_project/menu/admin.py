from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('menu',)
    fileldsets = (
        ('Добавить пункт меню', {
        'description': 'Блаблабла',
        'fields':(('menu', 'parent'), 'name', 'slug')
        }),
    )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
