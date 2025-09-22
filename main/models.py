import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('cap', 'Cap'),
        ('scarf', 'Scarf'),
        ('accessory', 'Accessory'),
    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0) # Jumlah stok
    is_official_merch = models.BooleanField(default=False) # Official merch
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M') # Size
    is_signed = models.BooleanField(default=False)  # Jersey yang ada tanda tangannya
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini
    
    

    def __str__(self):
        return self.name
    
    @property
    
    def is_low_stock(self):
        return self.stock < 10 # Buat meriksa jumlah stok nya kurang dari 10 apa engga
                                # Kalo iya dia bakal balikin True, yang kasih tanda kalo stok hampir habis.
    def increment_stock(self):
        self.stock += 1
        self.save() # Buat nambahin nilai stok sebanyak 1 dan menyimpan perubahan nya ke database
        
