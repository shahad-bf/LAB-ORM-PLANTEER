from django.contrib import admin
from .models import Plant, Comment


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_edible', 'created_at']
    list_filter = ['category', 'is_edible', 'created_at']
    search_fields = ['name', 'about', 'used_for']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('معلومات أساسية', {
            'fields': ('name', 'category', 'is_edible', 'image')
        }),
        ('التفاصيل', {
            'fields': ('about', 'used_for')
        }),
        ('معلومات النظام', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'plant', 'created_at']
    list_filter = ['created_at', 'plant__category']
    search_fields = ['full_name', 'content', 'plant__name']
    readonly_fields = ['created_at']
