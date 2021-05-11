from django.db import models
from django.contrib.auth.hashers import make_password

class UserModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32,null=True)

    def save(self, **kwargs):
        password = make_password(self.password)
        username = make_password(self.username)
        super().save(**kwargs)

    def __str__(self):
        return self.name
