from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.title