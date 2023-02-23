from django.db import models
# Create your models here.

import sqlite3


class Shopper(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'name - {self.name} //// password - {self.password} //// e-mail - {self.email} '
