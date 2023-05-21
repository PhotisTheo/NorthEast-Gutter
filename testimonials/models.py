from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Testimonials(models.Model):
    overview = models.TextField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.overview
