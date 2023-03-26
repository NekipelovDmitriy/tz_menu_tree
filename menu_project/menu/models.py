from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Название меню',
    )    
    slug = models.SlugField(
        max_length=255, unique=True,
    )

    class Meta:
        verbose_name = 'Меню'        

    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Пункт меню',
    )
    slug = models.SlugField(
        max_length=255, unique=True,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menuitems',
        blank=True,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='childs',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self) -> str:
        return self.name
