from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Plant, Comment
from .forms import PlantForm, CommentForm, PlantSearchForm


def all_plants(request):
    plants = Plant.objects.all()
    
    # Filter by category
    category = request.GET.get('category')
    if category:
        plants = plants.filter(category=category)
    
    # Filter by is_edible
    is_edible = request.GET.get('is_edible')
    if is_edible == 'true':
        plants = plants.filter(is_edible=True)
    elif is_edible == 'false':
        plants = plants.filter(is_edible=False)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        plants = plants.filter(
            Q(name__icontains=query) | 
            Q(about__icontains=query) |
            Q(used_for__icontains=query)
        )
    
    context = {
        'plants': plants,
        'categories': Plant.CATEGORY_CHOICES,
        'current_category': category,
        'current_is_edible': is_edible,
        'search_query': query,
    }
    
    return render(request, 'plants/all_plants.html', context)


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    comments = plant.comments.all()
    related_plants = plant.get_related_plants()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.plant = plant
            comment.save()
            messages.success(request, 'تم إضافة تعليقك بنجاح!')
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        comment_form = CommentForm()
    
    context = {
        'plant': plant,
        'comments': comments,
        'related_plants': related_plants,
        'comment_form': comment_form,
    }
    
    return render(request, 'plants/plant_detail.html', context)


def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة النبات بنجاح!')
            return redirect('plants:all_plants')
    else:
        form = PlantForm()
    
    context = {
        'form': form,
        'title': 'إضافة نبات جديد'
    }
    
    return render(request, 'plants/add_plant.html', context)


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث النبات بنجاح!')
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    
    context = {
        'form': form,
        'plant': plant,
        'title': 'تحديث النبات'
    }
    
    return render(request, 'plants/update_plant.html', context)


def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        plant.delete()
        messages.success(request, 'تم حذف النبات بنجاح!')
        return redirect('plants:all_plants')
    
    context = {
        'plant': plant
    }
    
    return render(request, 'plants/delete_plant.html', context)


def search_plants(request):
    form = PlantSearchForm(request.GET)
    plants = Plant.objects.none()
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        is_edible = form.cleaned_data.get('is_edible')
        
        plants = Plant.objects.all()
        
        if query:
            plants = plants.filter(
                Q(name__icontains=query) | 
                Q(about__icontains=query) |
                Q(used_for__icontains=query)
            )
        
        if category:
            plants = plants.filter(category=category)
        
        if is_edible == 'true':
            plants = plants.filter(is_edible=True)
        elif is_edible == 'false':
            plants = plants.filter(is_edible=False)
    
    context = {
        'form': form,
        'plants': plants,
    }
    
    return render(request, 'plants/search_plant.html', context)
