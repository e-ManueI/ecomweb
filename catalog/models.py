from audioop import reverse
from unicodedata import decimal
from django.db import models
from model_utils import Choices
from django.core.validators import MaxValueValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField('BodyType/Category', max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # TODO follow up this code below and slug
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name.upper()
    
    # TODO follow up this code below
    def get_absolute_url(self):
        return reverse('catalog_category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    prodcode = models.CharField(max_length=50)
    make = models.CharField('Make', max_length=50)
    prodmodel = models.CharField("Model", max_length=50, default='Null')
    name = models.CharField('Name', max_length=50)
    quantity = models.IntegerField('Quantity', validators=[MaxValueValidator(500)], default=0)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    STATUS = Choices('New', 'Used', 'Refurbished')
    state = models.CharField(choices=STATUS, default=STATUS.New, max_length=20)
    DRIVE = Choices('All Wheel Drive(AWD)', 'Front Wheel Drive(FWD)', 'Rear Wheel Drive(RWD)', '4 Wheel Drive(4WD)')
    drive = models.CharField('Drive', choices=DRIVE, default='Front Wheel Drive(FWD)', max_length=25)    
    TRANSMISSIONS = Choices('Manual', 'Automatic', 'Continously variable transmission(CVT)', 'Semi-Automatic', 'Dual-clutch')
    transmission = models.CharField(
        'Transmission Type', choices=TRANSMISSIONS, default=TRANSMISSIONS.Automatic, max_length=38)
    FUEL = Choices('Petrol', 'Diesel')
    fuel = models.CharField('Fuel Type', choices=FUEL, default=FUEL.Petrol, max_length=6)
    engine_size = models.DecimalField('Engine Size(Ltrs)', max_digits=3, decimal_places=3, default=0.0)
    engine_type = models.CharField('Engine Type', max_length=70)
    # steeringtype
    mileage = models.DecimalField('Mileage', max_digits=9, decimal_places=2, default=0.0)
    doors = models.PositiveIntegerField('Doors', validators=[MaxValueValidator(5)])
    seats = models.PositiveIntegerField(
        'Seats', validators=[MaxValueValidator(10)])
    bodycolor = models.CharField(max_length=50, default='White')
    fuel_consumption = models.DecimalField('Fuel Consumption/km', max_digits=4, decimal_places=2)
    # TODO deal with price
    price = models.PositiveIntegerField(validators=[MaxValueValidator(500000000)], default=0)
    old_price = models.PositiveIntegerField(blank=True, validators=[MaxValueValidator(500000000)], default=0)
    description = models.TextField()
    manufactured = models.DateField('Manufacture Date', blank=True)
    regdate = models.DateField('Registration Date', blank=True)
    # TODO limit price to be > 0
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    meta_keywords = models.CharField(
        "Meta keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(
        "Meta Description", max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name.upper()
    
    def get_absolute_url(self):
        return reverse('catalog_product', kwargs={'product_slug': self.slug})
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None