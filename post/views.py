from django.shortcuts import render
from .models import Post
from testimonials.models import Testimonials
from testimonials.forms import TestimonialsForm
from contact.models import Contact
from contact.forms import ContactForm
from django.http import HttpResponseRedirect


def index(request):
    submitted = False
    if request.method == "POST":
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = TestimonialsForm
        if 'submitted' in request.GET:
            submitted = True

    queryset = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:2]
    testimonials = Testimonials.objects.order_by('-timestamp')[0:4]
    form = TestimonialsForm
    context = {

        'object_list': queryset,
        'latest': latest,
        'testimonials': testimonials,
        'form': form,
        'submitted': submitted
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
    contact = Contact
    form = ContactForm
    context = {
        'contact': contact,
        'form': form,
        'submitted': submitted
    }
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})
