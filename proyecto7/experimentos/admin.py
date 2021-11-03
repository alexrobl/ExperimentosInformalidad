from django.contrib import admin
from proyecto7.experimentos.models import Set, Images, Experiment
from django.http import HttpResponse

from zipfile import ZipFile
import csv
# Register your models here.

def ExperimentToCSV(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


def ExperimentToZIP(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/zip')
    zipObj = ZipFile(response, 'w')
    
    for obj in queryset:
        zipObj.writestr(obj.video.name ,obj.video.path)
        
    response['Content-Disposition'] = 'attachment; filename=sample.zip'
    
    return response

@admin.register(Set,Images, Experiment)
class experimentsAdmin(admin.ModelAdmin):
    actions = [ExperimentToCSV, ExperimentToZIP]
