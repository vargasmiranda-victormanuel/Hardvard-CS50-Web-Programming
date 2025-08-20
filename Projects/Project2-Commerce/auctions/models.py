from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
    
class Listing(models.Model):
    header = models.CharField(max_length=128, db_index=True)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, 
        decimal_places=2, validators=[MinValueValidator(Decimal("0.1"))])
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
    closed_time = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='wins')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        # Use header (you don’t have `title`)
        seller_display = getattr(self.seller, "username", self.seller_id)
        winner_display = getattr(self.winner, "username", self.winner_id) if self.winner_id else "—"
        return f"{self.header} · seller={seller_display} · winner={winner_display}"
    
    class Meta:
        ordering = ["-is_active", "-created_at", "-id"]
        constraints = [
            models.CheckConstraint(
                name="listing_starting_bid_min_010",
                check=Q(starting_bid__gte=Decimal("0.10")),
            ),
            models.CheckConstraint(
                name="listing_closed_requires_time",
                check=Q(is_active=True) | Q(closed_time__isnull=False),
            ),
        ]
        indexes = [
            models.Index(fields=["is_active", "category", "-created_at"], name="idx_active_cat_created"),
        ]
    
    def clean(self):
        "validations of the information"
        super().clean()

        if not self.category_id:
            raise ValidationError({"category": "Category is required."})

        if not self.seller_id:
            raise ValidationError({"seller": "Seller is required."})
        
        if self.is_active is False and self.closed_time is None:
            self.closed_time = self.closed_time or timezone.now()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

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