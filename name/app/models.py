from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    imagelink = models.CharField(max_length=500)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return self.title
