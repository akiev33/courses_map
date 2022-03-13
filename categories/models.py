from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категории')
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        if self.sub_category:
            return f'ID: {self.id} -> {self.name}, Под категория: {self.sub_category}'
        return f'ID: {self.id}, Название: {self.name}'