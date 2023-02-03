from django.db import models


class User(models.Model):
    nick_name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nick_name
