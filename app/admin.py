from django.contrib import admin
from .models import Cidade, Ocupacao, InstituicaoEnsino, AreaSaber, Curso, Turma, Disciplina, Matricula, Avaliacao, Frequencia, Turnos, CursoDisciplina, AvaliacaoTipo, Pessoa, Autor

# Registro de modelos no Django Admin
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)
admin.site.register(Pessoa)
admin.site.register(Autor)
