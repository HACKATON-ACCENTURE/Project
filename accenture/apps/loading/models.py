from django.db import models

# Create your models here.
class Workshop(models.Model):
	name = models.CharField('Наименование цеха', max_length = 200)
	unit = models.CharField('Агрегат', max_length = 200)
	dStart = models.DateTimeField('Плановая дата')
	OccupiedPercentage = models.IntegerField()
	date = models.DateTimeField('Дата')

def __str__(self):
		return self.name