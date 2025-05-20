from django.contrib import admin
from .models import (
    Cidade, Instituicao, AreaSaber, Ocupacao, Pessoas, Cursos,
    PeriodoCurso, Disciplinas, Matricula, Avaliacoes,
)

admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(AreaSaber)
admin.site.register(Ocupacao)
admin.site.register(Pessoas)
admin.site.register(Cursos)
admin.site.register(PeriodoCurso)
admin.site.register(Disciplinas)
admin.site.register(Matricula)
admin.site.register(Avaliacoes)

