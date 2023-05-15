from django.shortcuts import render
from .models import Post
from testimonials.models import Testimonials


def index(request):
    queryset = Post.objects.filter(featured=True)

    latest = Post.objects.order_by('-timestamp')[0:2]
    testimonials = Testimonials.objects.order_by('-timestamp')[0:10]
    context = {

        'object_list': queryset,
        'latest': latest,
        'testimonials': testimonials
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})
