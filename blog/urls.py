from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import index, blog, contact, about, services, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('contact/', contact),
    path('about/', about),
    path('services/', services),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
