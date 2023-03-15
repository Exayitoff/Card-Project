from django.db import models

class Shaxs(models.Model):
  rasm = models.ImageField(upload_to='rasmla/')
  ism_familya = models.CharField(max_length=200)
  ishi = models.CharField(max_length=200)
  instagrami = models.CharField(max_length=200)
  telegrami = models.CharField(max_length=200)
  facebooki = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.ism_familya