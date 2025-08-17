from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"
    
class Listing(models.Model):
    header = models.CharField(max_length=128, db_index=True)
    description = models.TextField()
    starting_bid = models.DecimalField( max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.1"))])
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
    closed_time = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='wins')

    def __str__(self):
        return f"{self.title} by {self.seller} won by {self.winner}"
    
class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids", db_index=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids", db_index=True)
    amount = models.DecimalField( max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.1"))])

    def __str__(self):
        return f"Bid {self.amount} by {self.bidder} on {self.listing}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", db_index=True)
    body = models.TextField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist", db_index=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist", db_index=True)  