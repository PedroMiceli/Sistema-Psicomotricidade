from django.contrib import admin
from .models import Paciente, Anamnese, Conclusao, PrimeiraUnidadeFuncional, SegundaUnidadeFuncional, TerceiraUnidadeFuncional, DesenhoFiguraHumana

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Anamnese)
admin.site.register(Conclusao)
admin.site.register(PrimeiraUnidadeFuncional)
admin.site.register(SegundaUnidadeFuncional)
admin.site.register(TerceiraUnidadeFuncional)
admin.site.register(DesenhoFiguraHumana)
