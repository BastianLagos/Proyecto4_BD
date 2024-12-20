from django.db import models

class Pelicula(models.Model):
    nombre = models.TextField(max_length=200)
    foto = models.ImageField(upload_to="imagenes_bd/",null=True,blank=True)