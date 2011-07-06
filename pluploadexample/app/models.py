from django.db import models

# Create your models here.

class Article(models.Model):
    
    title = models.CharField(max_length=255)
    
    __unicode__ = lambda self: self.title
    
class Photo(models.Model):
    article = models.ForeignKey(Article)
    file = models.FileField(upload_to='files')