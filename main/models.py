from django.db import models


class Article(models.Model):
    title=models.CharField('Мавзуъ',max_length=50)
    text=models.TextField('Матн')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name='Макола'
        verbose_name_plural='Маколахо'
