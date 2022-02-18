from django.db import models


# Create your models here.
class CPPCode(models.Model):
    id = models.AutoField
    question = models.CharField(max_length=100000)
    code = models.CharField(max_length=10000000000)
    date = models.DateField()

    def __str__(self):
        return self.question
