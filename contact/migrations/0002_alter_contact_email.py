# Generated by Django 4.1.7 on 2023-05-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]