from django.db import models
from inventory.choices import STATUS_CHOICES, RESOURCE_TYPES


class Category(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    main_image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='not_available')
    specifications = models.JSONField(default=list, blank=True, null=True)
    potential_suppliers = models.ManyToManyField(
        Supplier, related_name='potential_suppliers', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"


class EquipmentImage(models.Model):
    image = models.ImageField(upload_to='equipment_images/')
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='resources/')
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='resources')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ResourceLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='extra_resources')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
