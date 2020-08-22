from django.db import models

# Create your models here.
class Sistema(models.Model):

    class SimOuNao(models.TextChoices):
        SIM = 'S', ('Sim')
        NAO = 'N', ('Não')

    Id = models.IntegerField(name="ID_SISTEMA",primary_key=True,db_column="ID_SISTEMA")
    Descricao = models.CharField(null=True,db_column="DSC_SISTEMA",max_length=100)
    DataInclusao = models.DateField(auto_now=True,db_column="DT_INCLUSAO")
    ChaveInclusao = models.CharField(null=False,db_column="CHAVE_INCLUSAO",max_length=50)
    DataAlteracao = models.DateField(null=True,db_column="DT_ALTERACAO")
    ChaveAlteracao = models.CharField(null=True,db_column="CHAVE_ALTERACAO",max_length=50)
    Excluido = models.CharField(null=False,db_column="FLAG_EXCLUIDO",max_length=1,
    choices=SimOuNao.choices,default="N")
    Tag = models.CharField(null=False,db_column="TAG_SISTEMA",max_length=50)

    class Meta:
        db_table = "MOBILE_CA_SISTEMA"



