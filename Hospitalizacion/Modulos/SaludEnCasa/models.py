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

class Auxiliar(models.Model):
    idUsuario = models.ForeignKey(Usuario, null= False, blank=False,on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto())

class Personal_Salud(models.Model):
    idUsuario = models.ForeignKey(Usuario, null= False, blank=False,on_delete=models.CASCADE)

    def nombrecompletop(self):
        return self.idUsuario.nombrecompleto()

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto())

class Medico(models.Model):
    idUsuario = models.ForeignKey(Personal_Salud,null= False, blank=False,on_delete=models.CASCADE)
    Especialidad = models.CharField(max_length=50,null=False) 
    Registro = models.CharField(max_length=50,null=False)

    def __str__(self):
        txt = "{} Nombre: {} Especialidad: {} Registro: {}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompletop(),self.Especialidad,self.Registro)

class Enfermero(models.Model):
    idUsuario = models.ForeignKey(Personal_Salud,null= False, blank=False,on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto())

class Paciente(models.Model):
    idUsuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    idMedico = models.ForeignKey(Medico,blank=False,on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=100, null=False)
    Ciudad = models.CharField(max_length=50, null=False)
    FechaNacimiento = models.DateField()
    Latitud = models.FloatField()
    Longitud = models.FloatField()

    def __str__(self):
        txt = "Id: {0} Nombre: {1}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto())

class Familiar(models.Model):
    idUsuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    idPaciente = models.ForeignKey(Paciente,null=False, blank=False, on_delete=models.CASCADE)
    Parentesco = models.CharField(max_length=30, null=False)
    Email = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "Id: {0}, Nombre: {1}, Id paciente:{2}"
        return txt.format(self.idUsuario,self.idUsuario.nombrecompleto(),self.idPaciente)

class Signos_Vitales(models.Model):
    idRegistro = models.PositiveIntegerField(primary_key=True,null=False,blank=False)
    idPaciente = models.ForeignKey(Paciente,null=False, blank=False, on_delete=models.CASCADE)
    signos = [
        ('O','Oximetría'),
        ('R','Frecuencia respiratoria'),
        ('C','Frecuencia cardiaca'),
        ('T','Temperatura'),
        ('A','Presion arterial'),
        ('G','Glicemias')
        ]
    Signo_Vital = models.CharField(max_length=1,choices= signos,null=False)
    Valor_Signo = models.FloatField(null=False)
    Fecha_Registro = models.DateField(auto_now=True)

    def __str__(self):
        txt = "Id paciente: {0}, Signo: {1}, Valor: {2}, Fecha: {3}"
        return txt.format(self.idPaciente,self.Signo_Vital,self.Valor_Signo,self.Fecha_Registro)



class Historia_Clinica(models.Model):
    id_Registro_Historia = models.PositiveIntegerField(primary_key=True,null=False,blank=False)
    idPaciente = models.ForeignKey(Paciente,null=False, blank=False, on_delete=models.CASCADE)
    idMedico = models.ForeignKey(Medico,null=False, blank=False,on_delete=models.CASCADE)
    Fecha_Registro_HC = models.DateField(auto_now=True)
    Detalles = models.CharField(max_length=5000,null=False)
    
    def __str__(self):
        txt = "Id historia: {0}, Id Paciente: {1}, Id Medico {2}, Fecha: {3}"
        return txt.format(self.id_Registro_Historia,self.idPaciente,self.idMedico,self.Fecha_Registro_HC)

class Sugerencias(models.Model):
    id_Sugerencia = models.PositiveIntegerField(primary_key=True,null=False,blank=False)
    id_Registro_Historia = models.ForeignKey(Historia_Clinica,null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Sugerencia = models.DateField(auto_now=True)
    Sugerencia = models.CharField(max_length=5000,null=False)

    def __str__(self):
        txt = "Id historia: {0}, Id Sugerencia: {1}, Fecha: {2}"
        return txt.format(self.id_Registro_Historia,self.id_Sugerencia,self.Fecha_Sugerencia)
