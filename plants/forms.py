from django import forms
from .models import Plant, Comment


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'اسم النبات'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'وصف مفصل عن النبات...'
            }),
            'used_for': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'الاستخدامات والفوائد...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_edible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'الاسم الكامل'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'اكتب تعليقك هنا...'
            }),
        }


class PlantSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ابحث عن النباتات...'
        })
    )
    category = forms.ChoiceField(
        choices=[('', 'جميع الفئات')] + Plant.CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    is_edible = forms.ChoiceField(
        choices=[
            ('', 'الكل'),
            ('true', 'صالح للأكل'),
            ('false', 'غير صالح للأكل')
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
