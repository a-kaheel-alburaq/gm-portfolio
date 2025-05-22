# home/models.py

from django.db import models
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class PortfolioItem(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField()

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(
        upload_to='category_icons/',
        validators=[FileExtensionValidator(['svg'])],
        help_text='Upload SVG icon file'
    )
    filter_class = models.CharField(max_length=50, help_text='CSS class used for filtering (e.g., filter-beef)')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    level = models.IntegerField(default=0, help_text='0 for main category, 1 for subcategory, 2 for sub-subcategory')
    order = models.IntegerField(default=0, help_text='Order in which the category appears')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Product Categories'
        ordering = ['level', 'order', 'name']

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

    def get_all_children(self):
        """Get all subcategories recursively"""
        children = list(self.subcategories.all())
        for child in self.subcategories.all():
            children.extend(child.get_all_children())
        return children

    def get_hierarchy(self):
        """Get the full hierarchy path of the category"""
        hierarchy = [self]
        parent = self.parent
        while parent is not None:
            hierarchy.insert(0, parent)
            parent = parent.parent
        return hierarchy

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    shop_link = models.URLField(max_length=500)
    image = models.ImageField(upload_to='products/')
    order = models.IntegerField(default=0, help_text='Order in which the product appears')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.category.name}"
