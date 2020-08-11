from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Product(models.Model):
    item = models.CharField(max_length=50, null=False)
    explanation = models.TextField(null=False)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    image = models.ImageField(upload_to = 'images/',null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)


class Review(models.Model):
    raiting = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')