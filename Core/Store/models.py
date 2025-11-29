from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    ProductName = models.CharField(max_length=150)
    ProductCategory = models.ForeignKey("Category",on_delete=models.CASCADE)
    ProductDescription = models.TextField(max_length=150)
    ProductQuantity = models.IntegerField(default=0)
    ProductPrice = models.DecimalField(max_digits=10,decimal_places=3)
    ProductImage = models.ImageField(upload_to="uploads/images/",null=True,)
    
    def __str__(self):
        return self.ProductName


class Category(models.Model):
    CategoryName = models.CharField(max_length=150)
    CategoryParent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child"
        )
    class Meta:
        verbose_name = "CategoryName"
        verbose_name_plural = 'Categories'
        unique_together = ('CategoryParent',)
        
    def __str__(self):
        full_path = [self.CategoryName]
        k = self.CategoryParent
        while k is not None:
            full_path.append(k.CategoryName)
            k = k.CategoryParent
        return ' -> '.join(full_path[::-1])
    
    @property
    def is_root(self):
        """Check if category is root (no CategoryParent)"""
        return self.CategoryParent is None
    
    @property
    def has_children(self):
        """Check if category has subcategories"""
        return self.children.exists()
    
    def get_all_children(self):
        """Get all children recursively"""
        children = list(self.children.all())
        for child in self.children.all():
            children.extend(child.get_all_children())
        return children