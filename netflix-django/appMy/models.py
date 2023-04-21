from django.db import models
from django.contrib.auth.models import User





class Category(models.Model):
    slug=models.SlugField(("Slug"))

    def __str__(self):
        return self.slug
    

class Tag(models.Model):
    slug=models.SlugField(("Tag"))

    def __str__(self):
        return self.slug

class CartFilm(models.Model):
    category=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag, verbose_name=("Tag"),blank=True)
    image=models.ImageField(("Film Resim"), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.category.slug
    
