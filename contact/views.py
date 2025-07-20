from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح! سنتواصل معك قريباً.')
            return redirect('contact:contact_us')
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'contact/contact.html', context)


def contact_messages(request):
    messages_list = ContactMessage.objects.all()
    
    context = {
        'messages': messages_list
    }
    
    return render(request, 'contact/contact_messages.html', context)
