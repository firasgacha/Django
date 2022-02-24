from django import forms

from .models import Projet


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ('nom_projet','duree_projet','temps_alloue_par_projet',
                  'besoins','est_valide','createur')