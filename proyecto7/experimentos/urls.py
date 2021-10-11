from django.urls import path
from experimentos.views import CreateExperimentView, new_experiment, get_experiment, show_disclaimerView

from . import views

urlpatterns = [
    path('', show_disclaimerView, name = 'disclaimer'),
    # path('test', ImageView.as_view(), name='index'),
    #path('new', CreateExperimentView.as_view(), name='Experiment'),
    path('new', new_experiment, name='Experiment'),
    # path('get', get_experiment, name = 'get'),
]