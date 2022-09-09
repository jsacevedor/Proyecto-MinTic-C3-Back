from tkinter import commondialog
from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.PositiveIntegerField(primary_key=True, null= False)
    Nombres = models.CharField(max_length=50,null= False)
    Apellidos = models.CharField(max_length=50,null= False)
    Clave = models.CharField(max_length=20,null= False)
    Telefono = models.PositiveIntegerField(null= False)
    sexos =[
        ('F','Femenino'),
        ('M','Masculino')
    ]
    Genero = models.CharField(max_length=1,choices= sexos)

    def __str__(self):
        txt = "{0} {1} {2} {3} {4} {5}"
        return txt.format(self.idUsuario,self.Nombres,self.Apellidos,self.Clave,self.Telefono,self.Genero)

