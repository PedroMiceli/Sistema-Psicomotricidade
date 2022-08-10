from django.urls import path, include
from .views import *


urlpatterns = [
    # Paciente

    path('paciente/create', PacienteCreate.as_view(), name='create-paciente'),
    path('paciente/update/<int:pk>', PacienteUpdate.as_view(), name='update-paciente'),
    path('paciente/details/<int:pk>', PacienteDetails.as_view(), name='details-paciente'),
    path('', PacientesList.as_view(), name='pacientes'),
    #path('/pacientes', PacientesList.as_view(), name='pacientes'),

    path('paciente-inativos/', PacientesInativosList.as_view(), name='pacientes-inativos'),

    # Anamnese
    path('paciente/anamnese', AnamneseCreate.as_view(), name='create-anamnese'),
    path('paciente/anamnese/<int:pk>', AnamneseUpdate.as_view(), name='update-anamnese'),
    path('paciente/details/<int:pk>/anamnese-pdf', render_pdf_anamnese, name='anamnese-pdf'),

    # Protocolo
    path('paciente/protocolo-primeira-unidade', PrimeiraUnidadeFuncionalCreate.as_view(), name='protocolo-primeira-unidade'),
    path('paciente/protocolo-segunda-unidade', SegundaUnidadeFuncionalCreate.as_view(), name='protocolo-segunda-unidade'),
    path('paciente/protocolo-terceira-unidade', TerceiraUnidadeFuncionalCreate.as_view(), name='protocolo-terceira-unidade'),
    path('paciente/protocolo-figura-humana', DesenhoFiguraHumanaCreate.as_view(), name='protocolo-figura-humana'),

    path('paciente/protocolo-primeira-unidade/<int:pk>', PrimeiraUnidadeFuncionalUpdate.as_view(), name='update-primeira-unidade'),
    path('paciente/protocolo-segunda-unidade/<int:pk>', SegundaUnidadeFuncionalUpdate.as_view(), name='update-segunda-unidade'),
    path('paciente/protocolo-terceira-unidade/<int:pk>', TerceiraUnidadeFuncionalUpdate.as_view(), name='update-terceira-unidade'),
    path('paciente/protocolo-figura-humana/<int:pk>', DesenhoFiguraHumanaUpdate.as_view(), name='update-figura-humana'),
    # Conclusao
    path('paciente/conclusao', ConclusaoCreate.as_view(), name='create-conclusao'),
    path('paciente/conclusao/<int:pk>', ConclusaoUpdate.as_view(), name='update-conclusao'),

    # Relatório
    path('paciente/details/<int:pk>/relatorio', RelatorioView.as_view(), name='relatorio'),
    path('paciente/details/<int:pk>/relatorio-pdf', render_pdf_view, name='relatorio-pdf'),
]