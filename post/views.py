from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
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
    most_recent = Post.objects.order_by('-timestamp')[:4]
    post_list = Post.objects.order_by('-timestamp')
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    post = paginator.get_page('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'post': post,

    }
    return render(request, 'blog.html', context)


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


def post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)
