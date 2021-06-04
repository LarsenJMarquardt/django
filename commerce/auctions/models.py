from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# auction listings, bids, comments, auction categories
class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    listing_date = models.DateField()
    image = models.URLField()

class Bids(models.Model):
    user_name = models.CharField(max_length=100)
    bid = models.IntegerField()
    bid_date = models.DateField()

class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=150)
    comment_date = models.DateField()

