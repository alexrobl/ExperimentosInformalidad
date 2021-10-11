from django.db import models
from django.db.models.fields import TextField, UUIDField
#from survey.models.survey import Survey


# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = TextField(blank=True)
    photo = models.ImageField(upload_to='experimentos/photos')

    def __str__(self):
        return self.name

class Experiment(models.Model):
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    order_imgs = models.CharField(max_length=300, blank=False)
    video = models.FileField(upload_to='experimentos/videos',blank=False)
    experiment_uuid = models.UUIDField()
    

    def __str__(self):
        return "el video {} se guardo con identificador {}".format(self.pk, self.experiment_uuid)
