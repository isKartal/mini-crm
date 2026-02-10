from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Deal(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    STATUS_CHOICES = (
        (NEW, 'Yeni'),
        (CONTACTED, 'İletişimde'),
        (WON, 'Kazanıldı'),
        (LOST, 'Kaybedildi'),
    )

    customer = models.ForeignKey(Customer, related_name='deals', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='deals', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    customer = models.ForeignKey(Customer, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
