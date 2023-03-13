from django.db import models

class User(models.Model):
    """ User Model Definition """
    
    username = models.CharField(
        max_length=150,
        unique=True
    )
    password = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.username