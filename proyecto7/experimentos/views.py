import uuid

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from proyecto7.experimentos.models import Experiment, Images
from django.views.generic import ListView, CreateView, TemplateView

from django.urls import reverse_lazy
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.base import ContentFile
# forms
from proyecto7.experimentos.forms.forms import ExperimentForm


class CreateExperimentView(CreateView):

    uuid_value = uuid.uuid4().hex

    """Create a new experiment"""
    template_name = 'Experiments/new.html'
    form_class = ExperimentForm
    success_url = "https://docs.google.com/forms/d/e/1FAIpQLSepEnFiXgL1ZZoJBEX8qIyW6xvtaVMQzqpAuc3QCr7u2xtuRg/viewform?entry.1332288676={}".format(uuid_value)
    #success_url = reverse_lazy('survey-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Imagenes'] = Images.objects.all().order_by('?')
        context['orden'] = [img.pk for img in context['Imagenes']]
        context['Uuid'] = self.uuid_value 
        return context

def new_experiment(request):
    Imagenes = Images.objects.all().order_by('?')
    orden = [img.pk for img in Imagenes]
    uuid_value = uuid.uuid4().hex
    success_url = "https://docs.google.com/forms/d/e/1FAIpQLSepEnFiXgL1ZZoJBEX8qIyW6xvtaVMQzqpAuc3QCr7u2xtuRg/viewform?entry.1332288676={}".format(uuid_value)
    if request.method == 'POST':
        video_data = request.FILES.get('data')
        uuid_data = request.POST.get('uuid')
        order_data = request.POST.get('order')
        save_experiment = Experiment(experiment_uuid=uuid_data,order_imgs=order_data)
        name_file = '{}.mp4'.format(uuid_data)
        save_experiment.video.save(name_file,ContentFile(video_data.read()))
        save_experiment.save()

        #return redirect("https://docs.google.com/forms/d/e/1FAIpQLSepEnFiXgL1ZZoJBEX8qIyW6xvtaVMQzqpAuc3QCr7u2xtuRg/viewform?entry.1332288676={}".format(uuid_value))
        #import pdb; pdb.set_trace()
        #Experiment.objects.create(order_imgs = order_data, experiment_uuid = uuid_data, video = (, ), )
    return render(
        request= request,
        template_name= 'Experiments/new.html',
        context= {
            'Imagenes':Imagenes,
            'orden':orden,
            'Uuid':uuid_value,
        }
    )

def get_experiment(request):
    Imagenes = Images.objects.all().order_by('?')
    orden = [img.pk for img in Imagenes]
    uuid_value = uuid.uuid4().hex
    success_url = "https://docs.google.com/forms/d/e/1FAIpQLSepEnFiXgL1ZZoJBEX8qIyW6xvtaVMQzqpAuc3QCr7u2xtuRg/viewform?entry.1332288676={}".format(uuid_value)
    if request.method == 'POST':
        video_data = request.FILES.get('data')
        uuid_data = request.POST.get('uuid')
        order_data = request.POST.get('order')
        save_experiment = Experiment(experiment_uuid=uuid_data,order_imgs=order_data)
        name_file = '{}.mp4'.format(uuid_data)
        save_experiment.video.save(name_file,ContentFile(video_data.read()))
        save_experiment.save()
        return redirect(success_url)
        #import pdb; pdb.set_trace()
        #Experiment.objects.create(order_imgs = order_data, experiment_uuid = uuid_data, video = (, ), )
    return render(
        request= request,
        template_name= 'Experiments/get.html',
        context= {
            'Imagenes':Imagenes,
            'orden':orden,
            'Uuid':uuid_value,
        }
    )

def show_disclaimerView(request):
    template_name = 'Experiments/Disclaimer.html'
    return render(request, template_name)
