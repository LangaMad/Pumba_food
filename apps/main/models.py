from django.db import models

# Create your models here.


class About_us(models.Model):
    history = models.TextField(verbose_name=' Наша История')
    mission = models.TextField(verbose_name=' Наша Миссия')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'








