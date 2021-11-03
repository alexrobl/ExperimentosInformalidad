from django.db import models
from django.db.models.fields import TextField, UUIDField,URLField
from tinymce.models import HTMLField
#from survey.models.survey import Survey


# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre conjunto de datos, Use su nomenclatura",)
    Image_instruccions = models.ImageField(upload_to='experimentos/instructions',verbose_name="Imagen con instrucciones",)
    disclaimer = HTMLField(verbose_name="Pegue aca su disclaimer y de estilos.")
    survey_url = URLField(max_length=200, verbose_name="URL Encuesta desde google forms, la url DEBE recibir un ID",)

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = TextField(blank=True)
    photo = models.ImageField(upload_to='experimentos/photos')
    set_relation = models.ForeignKey(
        'Set',
        on_delete=models.CASCADE,
        related_name="folder"
    )

    def __str__(self):
        return self.name

class Experiment(models.Model):
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    set_id = models.IntegerField()
    order_imgs = models.CharField(max_length=300, blank=False)
    video = models.FileField(upload_to='experimentos/videos',blank=False)
    experiment_uuid = models.UUIDField()
    

    def __str__(self):
        return "el video {} se guardo con identificador {}".format(self.pk, self.experiment_uuid)
