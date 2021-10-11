"""Experiment Forms"""
#django
from django import forms
# Models
from proyecto7.experimentos.models import Experiment

class ExperimentForm(forms.ModelForm):
    """Experiment model Form."""

    class Meta:
        model = Experiment
        fields = ('order_imgs','video','experiment_uuid')