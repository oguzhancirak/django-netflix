from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from appMy.models import CartFilm




class Profil(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to='profil', max_length=200)
   password = models.CharField(("Şifre"), max_length=50, null=True)
   password_active = models.BooleanField(("Şifrele"), default=False)
   films=models.ManyToManyField(CartFilm, verbose_name=("fimleri"),blank=True)
   
   def __str__(self):
      return self.user.username
   

@receiver(pre_delete, sender=Profil) # silinen objenin resmini media dosyasından kaldırır
def post_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Account(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Şifre"), max_length=50)
    tel =  models.CharField(("Telefon"), max_length=50)

    def __str__(self):
      return self.user.username
    

# @receiver(pre_delete, sender=Profil)
# def post_delete(sender, instance, **kwargs):
#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)
