from django.contrib import admin
from .models import (
    Cidade, Instituicao, AreaSaber, Ocupacao, Pessoas, Cursos, 
    PeriodoCurso, Disciplinas, Matricula, Avaliacoes, Frequencia,
    Turmas, Ocorrencias, DiciplinaCurso, TipoAvaliacao
)


class PessoaInline(admin.TabularInline):
    model = Pessoas
    extra = 1  # Número de pessoas adicionais para adicionar no admin

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos que serão exibidos na listagem de Ocupação
    search_fields = ('nome',)  # Campos que serão pesquisados
    inlines = [PessoaInline]  # Adiciona a tabela de pessoas no admin de ocupações

admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoas)



class CursoInline(admin.TabularInline):
    model = Cursos
    extra = 1  # Número de cursos adicionais para adicionar no admin

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos que serão exibidos na listagem de Instituição
    search_fields = ('nome',)  # Campos que serão pesquisados
    inlines = [CursoInline]  # Adiciona a tabela de cursos no admin de instituições

admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Cursos)






@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome', 'uf')



@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)







@admin.register(PeriodoCurso)
class PeriodoCursoAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    search_fields = ('numero',)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'instituicao', 'data_inicio', 'data_prev_termino')
    search_fields = ('pessoa__nome', 'curso__nome', 'instituicao__nome')
    list_filter = ('curso', 'instituicao')

@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'curso', 'disciplina')
    search_fields = ('descricao', 'curso__nome', 'disciplina__nome')
    list_filter = ('curso', 'disciplina')

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'disciplina', 'numero_faltas')
    search_fields = ('pessoa__nome', 'curso__nome', 'disciplina__nome')
    list_filter = ('curso', 'disciplina')

@admin.register(Turmas)
class TurmasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'periodo')
    search_fields = ('nome',)
    list_filter = ('periodo',)

@admin.register(Ocorrencias)
class OcorrenciasAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'pessoa', 'curso', 'disciplina')
    search_fields = ('descricao', 'pessoa__nome')
    list_filter = ('curso', 'disciplina', 'data')



@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
