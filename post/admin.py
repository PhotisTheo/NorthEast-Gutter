from django.contrib import admin

from .models import Author, Category, Post
from testimonials.models import Testimonials


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Testimonials)
