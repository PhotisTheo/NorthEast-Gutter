from django.contrib import admin

from .models import Author, Category, Post
from testimonials.models import Testimonials
from contact.models import Contact


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Testimonials)
admin.site.register(Contact)
