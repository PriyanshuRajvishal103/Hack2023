from django.db import models


class Information(models.Model):
    objects = None
    id = models.AutoField
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name
