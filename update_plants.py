#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planteer.settings')
django.setup()

from plants.models import Plant

def show_all_plants():
    """عرض جميع النباتات الموجودة"""
    plants = Plant.objects.all()
    print("=== النباتات الموجودة حالياً ===")
    for plant in plants:
        print(f"ID: {plant.id}")
        print(f"Name: {plant.name}")
        print(f"Category: {plant.get_category_display()}")
        print(f"Image: {plant.image}")
        print(f"About: {plant.about[:50]}...")
        print("-" * 50)

def update_plant_data():
    """تحديث بيانات النباتات"""
    
    # قائمة النباتات الجديدة مع صورها وتصنيفاتها
    plant_updates = [
        {
            'name': 'Peace Lily',
            'category': 'indoor',
            'image': 'baurry.jpg',
            'about': 'Peace lilies are elegant indoor plants with dark green leaves and beautiful white flowers that bloom year-round.',
            'used_for': 'Indoor decoration, air purification, low-light environments.',
            'is_edible': False
        },
        {
            'name': 'Mint',
            'category': 'herb',
            'image': 'lavender.jpg',
            'about': 'Mint is a refreshing herb with a cool, invigorating flavor. It\'s easy to grow and spreads quickly in gardens.',
            'used_for': 'Tea making, cooking, mojitos, natural breath freshener, digestive aid.',
            'is_edible': True
        },
        {
            'name': 'Blackberry',
            'category': 'fruit',
            'image': 'strubbary.webp',
            'about': 'Blackberries are delicious and nutritious fruits that grow on thorny bushes. Rich in vitamins and antioxidants.',
            'used_for': 'Fresh eating, jams, desserts, smoothies, baking.',
            'is_edible': True
        }
    ]
    
    # حذف النباتات الموجودة
    Plant.objects.all().delete()
    print("تم حذف جميع النباتات الموجودة")
    
    # إضافة النباتات الجديدة
    for plant_data in plant_updates:
        plant = Plant.objects.create(**plant_data)
        print(f"تم إضافة: {plant.name}")
    
    print("تم تحديث جميع النباتات بنجاح!")

if __name__ == "__main__":
    print("=== قبل التحديث ===")
    show_all_plants()
    
    print("\n=== تحديث البيانات ===")
    update_plant_data()
    
    print("\n=== بعد التحديث ===")
    show_all_plants()
