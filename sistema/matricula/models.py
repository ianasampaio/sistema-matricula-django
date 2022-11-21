from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome

class Aluno(models.Model):

    nome  = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome

    def getCurso(self):

        curso = self.vinculo_set.values('curso__nome','estado__estado').all()
        # return curso
        situacaoCurso = [value['curso__nome'] for value in curso if value['estado__estado'] == 'Vinculado' or value['estado__estado'] == 'Trancado']

        txtCursos = [value for value in situacaoCurso] 
        return txtCursos
        
    getCurso.short_description = 'Cursos'    

class Situacao(models.Model):
    choices = (
        ('Vinculado', 'Vinculado'),
        ('Trancado', 'Trancado'),
        ('Formado', 'Formado')
    )
    estado = models.CharField('Situação',max_length=20, choices=choices, blank=False, null=False)
    
    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"

    def __str__(self):
        return self.estado

class Vinculo(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    estado = models.ForeignKey(Situacao,verbose_name='Situação',on_delete=models.CASCADE)
    inicioSemestre =  models.PositiveIntegerField('Semestre de ingresso',blank=False, null=False)
    fimSemestre =  models.PositiveIntegerField('Semestre de conclusão',blank=True, null=True)

    class Meta:
        verbose_name = "Vínculo"
        verbose_name_plural = "Vínculos"
        ordering = ["-fimSemestre"]
    
    def __str__(self):
        return str(self.aluno) + ' , ' + str(self.curso)
