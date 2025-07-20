from django.core.management.base import BaseCommand
from plants.models import Plant

class Command(BaseCommand):
    help = 'Add plants with correct image paths from static/images folder'

    def handle(self, *args, **options):
        # Clear existing plants
        Plant.objects.all().delete()
        
        # Sample plants data with correct image paths
        plants_data = [
            {
                'name': 'Oleander',
                'about': 'Oleander is a beautiful flowering shrub with pink, white, or red blooms. It\'s drought-resistant and commonly used in landscaping.',
                'used_for': 'Ornamental decoration, landscaping, garden borders. Note: All parts are toxic if ingested.',
                'category': 'flower',
                'is_edible': False,
                'image': 'images/baurry.jpg',
            },
            {
                'name': 'Moringa Tree',
                'about': 'Moringa is known as the "miracle tree" for its exceptional nutritional value. Every part of the tree has beneficial uses.',
                'used_for': 'Nutritional supplements, leaves for cooking, seeds for oil, water purification.',
                'category': 'tree',
                'is_edible': True,
                'image': 'images/lavender.jpg',
            },
            {
                'name': 'Pomegranate',
                'about': 'Pomegranate is a fruit-bearing tree known for its antioxidant-rich red seeds. It\'s both ornamental and productive.',
                'used_for': 'Fresh fruit consumption, juice making, decorative purposes, traditional medicine.',
                'category': 'fruit',
                'is_edible': True,
                'image': 'images/strubbary.webp',
            },
            {
                'name': 'Sweet Basil',
                'about': 'Sweet basil is a popular culinary herb known for its aromatic leaves and distinctive flavor. It\'s commonly used in Mediterranean and Asian cuisine.',
                'used_for': 'Cooking, tea, natural pest control, aromatherapy. Essential in Italian cuisine and pesto making.',
                'category': 'herb',
                'is_edible': True,
                'image': 'images/baurry.jpg',
            },
            {
                'name': 'English Rose',
                'about': 'Classic English roses are renowned for their beautiful blooms and sweet fragrance. They are perfect for gardens and decorative purposes.',
                'used_for': 'Ornamental decoration, perfume making, rose water, dried petals for potpourri.',
                'category': 'flower',
                'is_edible': False,
                'image': 'images/lavender.jpg',
            },
            {
                'name': 'Aloe Vera',
                'about': 'Aloe vera is a succulent plant known for its medicinal properties. The gel inside its leaves has healing and moisturizing benefits.',
                'used_for': 'Skin care, burn treatment, hair conditioning, natural moisturizer, digestive health.',
                'category': 'succulent',
                'is_edible': True,
                'image': 'images/strubbary.webp',
            },
            {
                'name': 'Spider Plant',
                'about': 'Spider plants are popular indoor plants known for their long, thin leaves and air-purifying qualities. They\'re easy to care for and propagate.',
                'used_for': 'Air purification, indoor decoration, easy propagation for new plants.',
                'category': 'indoor',
                'is_edible': False,
                'image': 'images/baurry.jpg',
            },
            {
                'name': 'Tomato',
                'about': 'Tomatoes are versatile fruits commonly used as vegetables in cooking. They\'re rich in vitamins and perfect for home gardens.',
                'used_for': 'Fresh eating, salads, cooking, sauces, soups, canning for preservation.',
                'category': 'fruit',
                'is_edible': True,
                'image': 'images/baurry.jpg',
            },
            {
                'name': 'Mint',
                'about': 'Mint is a refreshing herb with a cool, invigorating flavor. It\'s easy to grow and spreads quickly in gardens.',
                'used_for': 'Tea making, cooking, mojitos, natural breath freshener, digestive aid.',
                'category': 'herb',
                'is_edible': True,
                'image': 'images/lavender.jpg',
            },
            {
                'name': 'Peace Lily',
                'about': 'Peace lilies are elegant indoor plants with dark green leaves and white blooms. They\'re known for their air-purifying abilities.',
                'used_for': 'Indoor decoration, air purification, low-light areas, office environments.',
                'category': 'indoor',
                'is_edible': False,
                'image': 'images/strubbary.webp',
            },
        ]

        for plant_data in plants_data:
            plant = Plant.objects.create(**plant_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created plant: {plant.name} with image: {plant.image}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {len(plants_data)} plants with correct image paths')
        )
