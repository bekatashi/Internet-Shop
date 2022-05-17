from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Images(models.Model):
    image = models.ImageField(upload_to='images/', )
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, related_name='image', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')

    def __str__(self):return f'image of {self.product}'