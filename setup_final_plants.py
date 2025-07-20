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

# Create ALL plants - old ones for homepage + new ones for all plants
plants_data = [
    # OLD PLANTS FOR HOMEPAGE (3 plants) - النباتات القديمة للصفحة الرئيسية
    {
        'name': 'Sweet Basil',
        'category': 'herb',
        'about': 'Sweet basil is a popular culinary herb known for its aromatic leaves and distinctive flavor.',
        'used_for': 'Cooking, pesto making, Italian cuisine, natural insect repellent',
        'is_edible': True,
        'image': 'strubbary.webp'  # التوت - صورة قديمة
    },
    {
        'name': 'Strawberry Plant',
        'category': 'fruit',
        'about': 'Strawberry plants produce sweet, red berries and are easy to grow in gardens or containers.',
        'used_for': 'Fresh eating, jams, desserts, vitamin C source, antioxidants',
        'is_edible': True,
        'image': 'baurry.jpg'  # الفراولة - صورة قديمة
    },
    {
        'name': 'Mint',
        'category': 'herb',
        'about': 'Mint is a refreshing herb with a cool, invigorating flavor. It grows quickly and spreads easily in gardens.',
        'used_for': 'Tea making, cooking, mojitos, natural breath freshener, digestive aid',
        'is_edible': True,
        'image': 'lavender.jpg'  # الروزماري - صورة قديمة
    },
    
    # NEW PLANTS (6 plants) - النباتات الجديدة بالصور الصحيحة
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

# Create all plants
for i, plant_data in enumerate(plants_data):
    plant = Plant.objects.create(**plant_data)
    if i < 3:
        print(f'🏠 Homepage Plant: {plant.name} ({plant.get_category_display()}) - Image: {plant.image}')
    else:
        print(f'📋 All Plants: {plant.name} ({plant.get_category_display()}) - Image: {plant.image}')

print(f'\n🎉 Successfully created {len(plants_data)} plants!')
print('📍 First 3 plants will show on homepage')
print('📍 All plants will show in All Plants page')

# Show final result
print('\n' + '='*60)
print('FINAL PLANTS STRUCTURE:')
print('='*60)

print('\n🏠 HOMEPAGE PLANTS (Latest 3):')
homepage_plants = Plant.objects.all().order_by('-id')[:3]
for plant in homepage_plants:
    print(f'  🌱 {plant.name} ({plant.get_category_display()}) → {plant.image}')

print(f'\n📋 ALL PLANTS PAGE (Total {Plant.objects.count()}):')
for category_code, category_name in Plant.CATEGORY_CHOICES:
    plants = Plant.objects.filter(category=category_code)
    if plants.exists():
        print(f'\n  {category_name} ({plants.count()} plants):')
        for plant in plants:
            print(f'    🌿 {plant.name} → {plant.image}')
