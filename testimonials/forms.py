from django import forms
from django.forms import ModelForm
from testimonials.models import Testimonials


class TestimonialsForm(ModelForm):
    class Meta:
        model = Testimonials
        fields = ('overview', 'name', 'company')
        labels = {
            'overview': '',
            'name': '',
            'company': '',
        }

        widgets = {
            'overview': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Testimonial'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
        }
