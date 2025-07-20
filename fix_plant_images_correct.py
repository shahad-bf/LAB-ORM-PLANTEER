#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planteer.settings')
django.setup()

from plants.models import Plant

# Delete all existing plants to start fresh
Plant.objects.all().delete()
print('Deleted all existing plants')

# Create plants with the EXACT images you added manually
plants_data = [
    # 🧄 Herbs (الأعشاب)
    {
        'name': 'Rosemary',
        'category': 'herb',
        'about': 'Rosemary is a fragrant evergreen herb with needle-like leaves. It\'s commonly used in cooking and has medicinal properties.',
        'used_for': 'Cooking, aromatherapy, improving memory, hair care, natural preservative',
        'is_edible': True,
        'image': 'aklel.jpg'  # إكليل الجبل
    },
    {
        'name': 'Sunflower',
        'category': 'herb',
        'about': 'Sunflower is a tall plant with large yellow flowers that follow the sun. The seeds are nutritious and oil-rich.',
        'used_for': 'Oil production, seeds for snacking, ornamental purposes, wildlife food',
        'is_edible': True,
        'image': 'sun_floor.jpg'  # دوار الشمس
    },
    
    # 🥦 Vegetables (الخضروات)
    {
        'name': 'Parsley',
        'category': 'vegetable',
        'about': 'Parsley is a bright green herb with flat or curly leaves. It\'s rich in vitamins and adds fresh flavor to dishes.',
        'used_for': 'Cooking garnish, vitamin C source, breath freshener, medicinal tea',
        'is_edible': True,
        'image': 'baqdones.jpg'  # بقدونس
    },
    {
        'name': 'Cucumber',
        'category': 'vegetable',
        'about': 'Cucumber is a refreshing vegetable with high water content. It\'s crisp, cool, and perfect for salads.',
        'used_for': 'Salads, skincare, hydration, pickling, cooling effect',
        'is_edible': True,
        'image': 'keyar.webp'  # خيار
    },
    {
        'name': 'Zucchini',
        'category': 'vegetable',
        'about': 'Zucchini is a versatile summer squash with tender skin and mild flavor. It\'s low in calories and high in nutrients.',
        'used_for': 'Cooking, baking, pasta substitute, grilling, soup making',
        'is_edible': True,
        'image': 'kosa.jpg'  # كوسا
    },
    
    # 🍉 Fruits (الفواكه)
    {
        'name': 'Watermelon',
        'category': 'fruit',
        'about': 'Watermelon is a large, sweet fruit with high water content. It\'s perfect for hot summer days and very refreshing.',
        'used_for': 'Fresh eating, juice making, hydration, summer snacks, vitamin A and C source',
        'is_edible': True,
        'image': 'watermelon.jpg'  # بطيخ
    }
]

# Create plants with correct images
for plant_data in plants_data:
    plant = Plant.objects.create(**plant_data)
    print(f'✅ Created: {plant.name} ({plant.get_category_display()}) - Image: {plant.image}')

print(f'\n🎉 Successfully created {len(plants_data)} plants with correct images!')

# Show final result by category
print('\n' + '='*50)
print('FINAL PLANTS BY CATEGORY:')
print('='*50)

for category_code, category_name in Plant.CATEGORY_CHOICES:
    plants = Plant.objects.filter(category=category_code)
    if plants.exists():
        print(f'\n{category_name} ({plants.count()} plants):')
        for plant in plants:
            print(f'  🌱 {plant.name} → {plant.image}')
