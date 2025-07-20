from django.core.management.base import BaseCommand
from plants.models import Plant

class Command(BaseCommand):
    help = 'Update plants with English names and categories'

    def handle(self, *args, **options):
        # Delete all existing plants
        Plant.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all existing plants'))

        # Create new plants with English names and categories
        plants_data = [
            # Herbs
            {
                'name': 'Rosemary',
                'category': 'herb',
                'about': 'Rosemary is a fragrant evergreen herb with needle-like leaves. It\'s commonly used in cooking and has medicinal properties.',
                'used_for': 'Cooking, aromatherapy, improving memory, hair care, natural preservative',
                'is_edible': True,
                'image': 'aklel.jpg'
            },
            {
                'name': 'Sunflower',
                'category': 'herb',
                'about': 'Sunflower is a tall plant with large yellow flowers that follow the sun. The seeds are nutritious and oil-rich.',
                'used_for': 'Oil production, seeds for snacking, ornamental purposes, wildlife food',
                'is_edible': True,
                'image': 'sun_floor.jpg'
            },
            
            # Vegetables
            {
                'name': 'Parsley',
                'category': 'vegetable',
                'about': 'Parsley is a bright green herb with flat or curly leaves. It\'s rich in vitamins and adds fresh flavor to dishes.',
                'used_for': 'Cooking garnish, vitamin C source, breath freshener, medicinal tea',
                'is_edible': True,
                'image': 'baqdones.jpg'
            },
            {
                'name': 'Cucumber',
                'category': 'vegetable',
                'about': 'Cucumber is a refreshing vegetable with high water content. It\'s crisp, cool, and perfect for salads.',
                'used_for': 'Salads, skincare, hydration, pickling, cooling effect',
                'is_edible': True,
                'image': 'keyar.webp'
            },
            {
                'name': 'Zucchini',
                'category': 'vegetable',
                'about': 'Zucchini is a versatile summer squash with tender skin and mild flavor. It\'s low in calories and high in nutrients.',
                'used_for': 'Cooking, baking, pasta substitute, grilling, soup making',
                'is_edible': True,
                'image': 'kosa.jpg'
            },
            
            # Fruits
            {
                'name': 'Watermelon',
                'category': 'fruit',
                'about': 'Watermelon is a large, sweet fruit with high water content. It\'s perfect for hot summer days and very refreshing.',
                'used_for': 'Fresh eating, juice making, hydration, summer snacks, vitamin A and C source',
                'is_edible': True,
                'image': 'watermelon.jpg'
            }
        ]

        # Create plants
        for plant_data in plants_data:
            plant = Plant.objects.create(**plant_data)
            self.stdout.write(
                self.style.SUCCESS(f'Created plant: {plant.name} ({plant.get_category_display()})')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(plants_data)} plants!')
        )
