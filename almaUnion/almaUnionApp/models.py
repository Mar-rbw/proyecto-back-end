from django.db import models
from almaUnionApp.choices.RolChoices import RolChoices
from almaUnionApp.choices.PlataformaChoices import PlataformaChoise
from almaUnionApp.choices.CategoriasChoices import CategoriasChoise
from .validators.validatorValidarRut import validar_rut

class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=45, unique=True)
    nombre_empresa = models.CharField(max_length=250, unique=True)
    categoria_empresa = models.CharField(max_length=20,choices=CategoriasChoise.choices, blank=True, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'empresas'
        db_table_comment = ' '
    
    def __str__(self):
        return self.nombre_empresa or self.rut_empresa

class Influencers(models.Model):
    
    id_influencer = models.AutoField(primary_key=True)
    rut_influencer = models.CharField(max_length=12, unique=True, validators=[validar_rut])
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_pat = models.CharField(max_length=50, blank=True, null=True)
    apellido_mat = models.CharField(max_length=50, blank=True, null=True)
    categoria_influencer = models.CharField(max_length=20,choices=CategoriasChoise.choices, blank=True, null=True)
    seguidores = models.BigIntegerField(blank=True, null=True)
    prom_views = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Influencer'
        verbose_name_plural = 'Influencers'
        db_table = 'influencers'
        
    def __str__(self):
        return f"{self.nombre} {self.apellido_pat} - {self.rut_influencer}"

class Campanas(models.Model):
    id_campana = models.AutoField(primary_key=True)
    id_empresa_campanas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    nombre_campana = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'
        db_table = 'campanas'
    
    def __str__(self):
        return self.nombre_campana or f"Campaña #{self.id_campana}"


class Colaboraciones(models.Model):
    id_colaboracion = models.AutoField(primary_key=True)
    id_influencer_colaboracion = models.ForeignKey(Influencers, models.CASCADE)
    id_campana_colaboracion = models.ForeignKey(Campanas, models.CASCADE)
    id_empresa_colaboracion = models.ForeignKey(Empresas, models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)
    pago_acordado = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name = 'Colaboracion'
        verbose_name_plural = 'Colaboraciones'
        db_table = 'colaboraciones'


class MetricasH(models.Model):
    id_metrica = models.AutoField(primary_key=True)
    id_influencer_metricas = models.ForeignKey(Influencers, models.CASCADE)
    id_empresa_metricas = models.ForeignKey(Empresas, models.CASCADE)
    nombre_metrica = models.CharField(max_length=250, blank=True, null=True)
    plataforma = models.CharField(max_length=20, choices=PlataformaChoise.choices, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    video = models.URLField(max_length=150, blank=True, null=False)
    vistas = models.BigIntegerField(blank=True, null=True)
    seguidores = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    comentarios = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Metrica Historica'
        verbose_name_plural = 'Metricas Historicas'
        db_table = 'metricas_h'


class RedesSociales(models.Model):
    id_red_social = models.AutoField(primary_key=True)
    id_empresa_redes = models.ForeignKey(Empresas, models.CASCADE)
    id_influencer_redes = models.ForeignKey(Influencers, models.CASCADE)
    plataforma = models.CharField(
        max_length=20,
        choices=PlataformaChoise.choices,
        blank=True)
    canal = models.URLField(max_length=150, blank=True, null=False)
    user_name = models.CharField(max_length=150, blank=True, null=True)
    seguidores = models.BigIntegerField(blank=True, null=True)
    vistas = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        db_table = 'redes_sociales'
        db_table_comment = ' '


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=15,choices= RolChoices.choices)
    verificado = models.BooleanField(default=False)
    imagen_perfil =models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
    id_empresa_usuarios = models.ForeignKey(Empresas, models.CASCADE)
    id_influencer_usuarios = models.ForeignKey(Influencers, models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'