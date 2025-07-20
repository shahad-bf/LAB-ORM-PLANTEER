#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planteer.settings')
django.setup()

from plants.models import Plant

# Add more plants to make the site more diverse
additional_plants = [
    # More Herbs
    {
        'name': 'Mint',
        'category': 'herb',
        'about': 'Mint is a refreshing herb with a cool, invigorating flavor. It grows quickly and spreads easily in gardens.',
        'used_for': 'Tea making, cooking, mojitos, natural breath freshener, digestive aid',
        'is_edible': True,
        'image': 'lavender.jpg'  # Using existing image
    },
    {
        'name': 'Basil',
        'category': 'herb',
        'about': 'Sweet basil is a popular culinary herb known for its aromatic leaves and distinctive flavor.',
        'used_for': 'Cooking, pesto making, Italian cuisine, natural insect repellent',
        'is_edible': True,
        'image': 'strubbary.webp'  # Using existing image
    },
    
    # More Vegetables
    {
        'name': 'Strawberry Plant',
        'category': 'fruit',
        'about': 'Strawberry plants produce sweet, red berries and are easy to grow in gardens or containers.',
        'used_for': 'Fresh eating, jams, desserts, vitamin C source, antioxidants',
        'is_edible': True,
        'image': 'baurry.jpg'  # Using existing image
    }
]

# Create additional plants
for plant_data in additional_plants:
    # Check if plant already exists
    if not Plant.objects.filter(name=plant_data['name']).exists():
        plant = Plant.objects.create(**plant_data)
        print(f'Added plant: {plant.name} ({plant.get_category_display()})')
    else:
        print(f'Plant {plant_data["name"]} already exists')

print(f'\nTotal plants in database: {Plant.objects.count()}')

# Show all plants by category
print('\n=== PLANTS BY CATEGORY ===')
for category_code, category_name in Plant.CATEGORY_CHOICES:
    plants = Plant.objects.filter(category=category_code)
    print(f'\n{category_name} ({plants.count()} plants):')
    for plant in plants:
        print(f'  - {plant.name} (Image: {plant.image})')
