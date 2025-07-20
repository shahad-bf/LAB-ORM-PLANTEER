from django.core.management.base import BaseCommand
from plants.models import Plant

class Command(BaseCommand):
    help = 'Setup final plants - old ones for homepage, new ones for all plants'

    def handle(self, *args, **options):
        # Delete all existing plants
        Plant.objects.all().delete()
        self.stdout.write('Deleted all existing plants')

        # Create all plants
        plants_data = [
            # OLD PLANTS FOR HOMEPAGE (3 plants)
            {
                'name': 'Sweet Basil',
                'category': 'herb',
                'about': 'Sweet basil is a popular culinary herb known for its aromatic leaves.',
                'used_for': 'Cooking, pesto making, Italian cuisine',
                'is_edible': True,
                'image': 'strubbary.webp'
            },
            {
                'name': 'Strawberry Plant',
                'category': 'fruit',
                'about': 'Strawberry plants produce sweet, red berries and are easy to grow.',
                'used_for': 'Fresh eating, jams, desserts, vitamin C source',
                'is_edible': True,
                'image': 'baurry.jpg'
            },
            {
                'name': 'Mint',
                'category': 'herb',
                'about': 'Mint is a refreshing herb with a cool, invigorating flavor.',
                'used_for': 'Tea making, cooking, mojitos, breath freshener',
                'is_edible': True,
                'image': 'lavender.jpg'
            },
            
            # NEW PLANTS (6 plants)
            {
                'name': 'Rosemary',
                'category': 'herb',
                'about': 'Rosemary is a fragrant evergreen herb with needle-like leaves.',
                'used_for': 'Cooking, aromatherapy, improving memory',
                'is_edible': True,
                'image': 'aklel.jpg'
            },
            {
                'name': 'Sunflower',
                'category': 'herb',
                'about': 'Sunflower is a tall plant with large yellow flowers.',
                'used_for': 'Oil production, seeds for snacking',
                'is_edible': True,
                'image': 'sun_floor.jpg'
            },
            {
                'name': 'Parsley',
                'category': 'vegetable',
                'about': 'Parsley is a bright green herb rich in vitamins.',
                'used_for': 'Cooking garnish, vitamin C source',
                'is_edible': True,
                'image': 'baqdones.jpg'
            },
            {
                'name': 'Cucumber',
                'category': 'vegetable',
                'about': 'Cucumber is a refreshing vegetable with high water content.',
                'used_for': 'Salads, skincare, hydration',
                'is_edible': True,
                'image': 'keyar.webp'
            },
            {
                'name': 'Zucchini',
                'category': 'vegetable',
                'about': 'Zucchini is a versatile summer squash with tender skin.',
                'used_for': 'Cooking, baking, pasta substitute',
                'is_edible': True,
                'image': 'kosa.jpg'
            },
            {
                'name': 'Watermelon',
                'category': 'fruit',
                'about': 'Watermelon is a large, sweet fruit with high water content.',
                'used_for': 'Fresh eating, juice making, hydration',
                'is_edible': True,
                'image': 'watermelon.jpg'
            }
        ]

        # Create plants
        for plant_data in plants_data:
            plant = Plant.objects.create(**plant_data)
            self.stdout.write(f'Created: {plant.name} ({plant.get_category_display()}) - {plant.image}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(plants_data)} plants!')
        )
        
        # Show homepage plants
        self.stdout.write('\nHomepage plants (latest 3):')
        homepage_plants = Plant.objects.all().order_by('-id')[:3]
        for plant in homepage_plants:
            self.stdout.write(f'  - {plant.name} → {plant.image}')
