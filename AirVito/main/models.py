from django.db import models


class Categories(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    name = models.CharField('name', max_length=50)
    image = models.TextField('image')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

