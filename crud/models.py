from django.db import models


class Concern(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Концерн'
        verbose_name_plural = 'Концерны'


class Car(models.Model):
    brand = models.CharField(max_length=25, verbose_name='Бренд')
    CHOICES = [
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('газ', 'газ'),
        ('гибрид', 'гибрид'),
    ]
    engine = models.CharField(max_length=25, choices=CHOICES, verbose_name='Двигатель')
    year = models.IntegerField(null=True, verbose_name='Год сборки')
    color = models.CharField(max_length=15, null=True, verbose_name='Цвет')
    concern = models.ForeignKey(Concern, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Концерн')
    showroom = models.ManyToManyField('Showroom', null=True, blank=True, verbose_name='Автосалон')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Showroom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

