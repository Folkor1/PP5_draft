from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    Contact view
    """
    contact = get_object_or_404(Contact, pk=name)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'We will be in touch with you shortly.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to send the message.')
    else:
        form = ContactForm(instance=contact)

    template = 'contact/contact.html'
    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, template, context)
