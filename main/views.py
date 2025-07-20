from django.shortcuts import render
from plants.models import Plant


def home(request):
    # Get the last 3 plants for the homepage (old plants: Sweet Basil, Strawberry, Mint)
    featured_plants = Plant.objects.all().order_by('-id')[:3]
    
    context = {
        'featured_plants': featured_plants,
        'total_plants': Plant.objects.count(),
    }
    
    return render(request, 'main/index.html', context)
