import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nick_name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nick_name
