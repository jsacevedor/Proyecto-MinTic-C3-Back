from django.contrib import admin
from Modulos.SaludEnCasa.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Auxiliar)
admin.site.register(Personal_Salud)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Signos_Vitales)
admin.site.register(Historia_Clinica)
admin.site.register(Sugerencias)