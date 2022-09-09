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

    def nombrecompleto(self):
        txt = "{0} {1}"
        return txt.format(self.Nombres,self.Apellidos)

    def __str__(self):
        txt = "{0} {1} {2} {3} {4} {5}"
        return txt.format(self.idUsuario,self.Nombres,self.Apellidos,self.Clave,self.Telefono,self.Genero)

class Paciente(models.Model):
    idUsuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=100, null=False)
    Ciudad = models.CharField(max_length=50, null=False)
    FechaNacimiento = models.DateField()
    Latitud = models.FloatField()
    Longitud = models.FloatField()

    def __str__(self):
        txt = "Id: {0} Nombre: {1}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto())
