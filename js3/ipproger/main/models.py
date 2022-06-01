
from django.db import models

# Create your models here.



class Articles(models.Model):
    title = models.CharField('Район + период', max_length=500)
    time = models.DateTimeField('Время', max_length=500)
    
    def __str__(self):
        return self.title


class Articles_2(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    anons = models.CharField('Имя расходов', max_length=500)
    numb = models.IntegerField('Цифра расходов')

    def __str__(self):
        return self.anons
 