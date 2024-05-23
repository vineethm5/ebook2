from django.db import models

# Create your models here.
class ebookss(models.Model):
    title=models.TextField(max_length=100,default='Test')
    summary=models.TextField(max_length=100,default='Test')
    pages=models.TextField(max_length=100,default='Test')
    pdf=models.FileField(upload_to='pdfs/',default='Test')
    author=models.TextField(max_length=100,default='Test')
    category=models.TextField(max_length=100, default='Test')
    

def __str__(self):
    return f'{self.title}'