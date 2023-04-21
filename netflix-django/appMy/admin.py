from django.contrib import admin
from .models import CartFilm,Category,Tag

class CartFilmAdmin(admin.ModelAdmin):
    list_display=("category",)
    

class TagAdmin(admin.ModelAdmin):
    list_display=("slug",)


admin.site.register(CartFilm,CartFilmAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category)