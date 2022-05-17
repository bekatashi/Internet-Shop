from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to='images/', )
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, related_name='image', on_delete=models.CASCADE, required=True)


