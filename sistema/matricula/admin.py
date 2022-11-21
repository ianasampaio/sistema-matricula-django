from django.contrib import admin

from .models import Aluno,Curso,Situacao,Vinculo

class CursoAdmin(admin.ModelAdmin):
    fields = ['nome']

admin.site.register(Curso,CursoAdmin)

class SituacaoAdmin(admin.ModelAdmin):
    fields = ['estado']

admin.site.register(Situacao,SituacaoAdmin)

class VinculoInline(admin.TabularInline):
    model = Vinculo
    extra = 1
    # list_display = ('nome','curso','estado','iniciosemestre','fimSemestre')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','getCurso')
    inlines = [VinculoInline]
admin.site.register(Aluno, AlunoAdmin)
