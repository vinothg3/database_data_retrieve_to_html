from django.db import models

# Create your models here.
class Topic(models.Model):
    Table_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Table_name
class Webpage(models.Model):
    Table_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField()
    def __str__(self):
        return self.name
class Access(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100,unique=True)
    date=models.DateField()
    def __str__(self) :
        return self.author
