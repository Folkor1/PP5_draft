from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    Contact view
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'We will be in touch with you shortly.')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send the message.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, template, context)
