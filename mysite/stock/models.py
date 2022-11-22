from django.db import models

class Valuts(models.Model):
    val =models.CharField(max_length=10)
    kurs =models.FloatField()
    val_so = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
    def __str__(self):        return self.val

class Category(models.Model):
    cat = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):        return self.val


class Products(models.Model):
    public = models.BooleanField(default=True)
    group = models.ForeignKey(Category, on_delete=models.PROTECT)
    UUID = models.IntegerField('UUID')
    type = models.CharField('Тип', max_length=36)
    cod = models.CharField('Код', max_length=36)
    name = models.CharField('Наименование', max_length=50)
    image = models.ImageField(null = True, blank = True, upload_to='images/', verbose_name = 'Изображение', max_length=100)
    discription = models.TextField('Описание', max_length=200)
    out_cod = models.CharField('Внешний код', max_length=36)
    article = models.CharField('Артикул', max_length=36)
    price = models.IntegerField('Цена')
    valut = models.ForeignKey(Valuts,on_delete=models.PROTECT)
    in_price = models.IntegerField('Закупоная цена')
    #valut_in_price = models.ForeignKey(Valuts, on_delete=models.PROTECT)
    shtrih  = models.IntegerField('Штрих код ')
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):        return self.name


BANKS = [
        ('ATYNKZKA', 'Altyn Bank'),
        ('KINCKZKA', 'Bank RBK'),
        ('TSESKZKA', 'First Heartland Jýsan Bank'),
        ('IRTYKZKA', 'ForteBank'),
        ('CASPKZKA', 'Kaspi Bank'),
        ('ALFAKZKA', 'АО ДБ «Есо Center Bank»'),
        ('KSNVKZKA', 'Банк Фридом Финанс Казахстан'),
        ('KCJBKZKX', 'Банк ЦентрКредит'),
        ('BKCHKZKA', 'ДБ "Банк Китая в Казахстане"'),
        ('KZIBKZKA', 'ДБ «Национальный Банк Пакистана»'),
        ('INLMKZKA', 'ДБ  АО"Банк Хоум Кредит"'),
        ('SABRKZKA', 'ДБ АО «Сбербанк России»'),
        ('VTBAKZKZ', 'ДО АО Банк ВТБ (Казахстан)'),
        ('EURIKZKA', 'Евразийский Банк'),
        ('ZAJSKZ22', 'Заман-Банк'),
        ('HLALKZKZ', 'Исламский Банк "Al-Hilal"'),
        ('HSBKKZKX', 'Народный сберегательный банк Казахстана'),
        ('NURSKZKX', 'Нурбанк'),
        ('HCSKKZKA', 'Отбасы банк'),
        ('CITIKZKA', 'Ситибанк Казахстан'),
        ('ICBKKZKX', 'ТП Банк Китая в Алматы'),
        ('SHBKKZKA', 'Шинхан Банк Казахстан'),
        ('KKMFKZ2A', 'РГУ "КОМИТЕТ КАЗНАЧЕЙСТВА МИНИСТЕРСТВА ФИНАНСОВ РК"'),
    ]
class Company(models.Model):
    iin = models.IntegerField('ИИН')
    name = models.CharField('Наименование', max_length=50)
    address = models.CharField('Адрес', max_length=120)
    BANKS = [
        ('ATYNKZKA', 'Altyn Bank'),
        ('KINCKZKA', 'Bank RBK'),
        ('TSESKZKA', 'First Heartland Jýsan Bank'),
        ('IRTYKZKA', 'ForteBank'),
        ('CASPKZKA', 'Kaspi Bank'),
        ('ALFAKZKA', 'АО ДБ «Есо Center Bank»'),
        ('KSNVKZKA', 'Банк Фридом Финанс Казахстан'),
        ('KCJBKZKX', 'Банк ЦентрКредит'),
        ('BKCHKZKA', 'ДБ "Банк Китая в Казахстане"'),
        ('KZIBKZKA', 'ДБ «Национальный Банк Пакистана»'),
        ('INLMKZKA', 'ДБ  АО"Банк Хоум Кредит"'),
        ('SABRKZKA', 'ДБ АО «Сбербанк России»'),
        ('VTBAKZKZ', 'ДО АО Банк ВТБ (Казахстан)'),
        ('EURIKZKA', 'Евразийский Банк'),
        ('ZAJSKZ22', 'Заман-Банк'),
        ('HLALKZKZ', 'Исламский Банк "Al-Hilal"'),
        ('HSBKKZKX', 'Народный сберегательный банк Казахстана'),
        ('NURSKZKX', 'Нурбанк'),
        ('HCSKKZKA', 'Отбасы банк'),
        ('CITIKZKA', 'Ситибанк Казахстан'),
        ('ICBKKZKX', 'ТП Банк Китая в Алматы'),
        ('SHBKKZKA', 'Шинхан Банк Казахстан'),
        ('KKMFKZ2A', 'РГУ "КОМИТЕТ КАЗНАЧЕЙСТВА МИНИСТЕРСТВА ФИНАНСОВ РК"'),
    ]
    bik =models.CharField(max_length=8, choices= BANKS, null = True)
    iik = models.CharField('Наименование', max_length=21)
    phone = models.IntegerField('Телефон', null = True)
    contact = models.CharField('Контакт', max_length=120,null = True)
    email = models.EmailField ('email', max_length=120, null = True)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):        return self.name






