from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20, default='Unsold')
    item_image = models.ImageField(default='default_item.jpg', upload_to='item_pics')
    bid = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    bid_phone = models.CharField(max_length=10, default='XXXXXXXXXX')
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    