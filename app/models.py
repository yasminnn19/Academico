from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do saber")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupaçao")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Cursos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.CharField(max_length=4, verbose_name="Carga horaria total")
    duracao_meses = models.CharField(max_length=2, verbose_name="Duração meses")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Nome da instituição")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class PeriodoCurso(models.Model):
    numero = models.IntegerField(verbose_name="Numero periodo")

    def __str__(self):
        return f"{self.numero}"

    class Meta:
        verbose_name = "Periodo do curso"
        verbose_name_plural = "Periodos do curso"


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_prev_termino = models.DateField(verbose_name="Data previsão termino")

    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_prev_termino}"

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"


class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")