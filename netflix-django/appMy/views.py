from django.shortcuts import render
from appUser.views import Profil
from .models import CartFilm,Category

# Create your views here.


def index(request):
   context={}
   return render(request, 'index.html', context)


def netflixPage(request,id,film_slug):
   profil = Profil.objects.get(id=id)

   if film_slug == "dizi" or film_slug == "film":
      films = CartFilm.objects.filter(category__slug=film_slug)
   elif film_slug == "gundem":
      films = CartFilm.objects.filter(tag__slug=film_slug)
   elif film_slug == "listem":
      films=CartFilm.objects.filter(profil=profil)
   else:
      film_slug="all"
      films=CartFilm.objects.all()

   if request.method == "POST":
      button=request.POST.get("submit")
      if button == "btn-film":
         film=request.POST.get("film-id")
         profil.films.add(film)
         profil.save()
      if button == "btn-cikar":
         film=request.POST.get("film-id")
         profil.films.remove(film)
         profil.save()

   context = {
      "profil":profil,
       "films": films,
       
   }
   return render(request, 'netflix.html', context)


