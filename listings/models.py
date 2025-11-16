#!/usr/bin/env python3
"""Models for the listings application."""
import uuid
from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """Model representing a property listing."""
    
    listing_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='listings'
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title} - {self.location}"


class Booking(models.Model):
    """Model representing a booking."""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    
    booking_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Booking {self.booking_id} - {self.listing.title}"


class Review(models.Model):
    """Model representing a review."""
    
    review_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['listing', 'user']
        
    def __str__(self):
        return f"Review by {self.user.username} - {self.rating} stars"
