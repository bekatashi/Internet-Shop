from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()


class Likes(models.Model):
    # product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self): return f'{self.product} liked'
