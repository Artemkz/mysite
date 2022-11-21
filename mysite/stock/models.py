from django.db import models


class Products(models.Model):
    public = models.BooleanField(default=True)
    group = models.CharField('Группа', max_length=25)
    UUID = models.IntegerField('UUID')
    type = models.CharField('Тип', max_length=36)
    cod = models.CharField('Код', max_length=36)
    name = models.CharField('Наименование', max_length=50)
    image = models.ImageField()
    discription = models.TextField('Описание', max_length=200)
    out_cod = models.CharField('Внешний код', max_length=36)
    article = models.CharField('Артикул', max_length=36)
    price = models.IntegerField('Цена')
    valut = models.CharField('Валюта', max_length=3)
    in_price = models.IntegerField('Закупоная цена')
    valut_in_price = models.CharField('Валюта Закупоной цены', max_length=3)
    shtrih  = models.IntegerField('Штрих код ')
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





