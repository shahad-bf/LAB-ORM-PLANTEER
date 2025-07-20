from django.db import models
from django.utils import timezone
from django.urls import reverse


class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('fruit', 'Fruit'),
        ('vegetable', 'Vegetable'),
        ('herb', 'Herb'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Plant Name")
    about = models.TextField(verbose_name="About Plant")
    used_for = models.TextField(verbose_name="Uses")
    image = models.ImageField(upload_to='plants/', verbose_name="Plant Image")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Category")
    is_edible = models.BooleanField(default=False, verbose_name="Edible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plants:plant_detail', kwargs={'plant_id': self.pk})

    def get_related_plants(self):
        return Plant.objects.filter(category=self.category).exclude(id=self.id)[:3]


class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    content = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"تعليق {self.full_name} على {self.plant.name}"
