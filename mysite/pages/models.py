from django.db import models

class Cosmonaut(models.Model):
    name = models.CharField('ФИО космонавта', max_length=200)
    birth_date = models.DateField('Дата рождения')
    birth_place = models.CharField('Место рождения', max_length=300)
    first_flight = models.DateField('Первый полет')
    total_flights = models.IntegerField('Количество полетов')
    total_space_time = models.CharField('Общее время в космосе', max_length=100)
    eva_count = models.IntegerField('Выходы в открытый космос', default=0)
    eva_time = models.CharField('Время в открытом космосе', max_length=100, blank=True)
    achievements = models.TextField('Достижения и рекорды')
    biography = models.TextField('Биография')
    photo = models.ImageField('Фотография', upload_to='cosmonauts/', blank=True)
    order = models.IntegerField('Порядок отображения', default=0)
    
    class Meta:
        verbose_name = 'Космонавт'
        verbose_name_plural = 'Космонавты'
        ordering = ['order']
    
    def __str__(self):
        return self.name