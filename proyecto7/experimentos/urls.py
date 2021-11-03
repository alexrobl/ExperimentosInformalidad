from django.urls import path
from experimentos.views import show_instructions, CreateExperimentView, new_experiment, get_experiment, show_disclaimerView,setListView

from . import views

urlpatterns = [
    path('',setListView.as_view(), name = 'set_list'),
    path('instructions/<int:id>/', show_instructions, name = 'instructions'),
    path('disclaimer/<int:id>/', show_disclaimerView, name = 'disclaimer'),
    # path('test', ImageView.as_view(), name='index'),
    #path('new', CreateExperimentView.as_view(), name='Experiment'),
    path('new/<int:id>/', new_experiment, name='Experiment'),
    # path('get', get_experiment, name = 'get'),
]