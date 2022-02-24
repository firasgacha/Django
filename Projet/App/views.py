from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .forms import AddProjectForm
from .models import Projet


def index(request):
    return HttpResponse('Bonjour 4 twin 4')


def index_param(request, classe):
    return HttpResponse('Bonjour 4 twin %s' % classe)


def index_template(request):
    # Django template in language DTL
    return render(request, 'App/index.html')


def Affiche(request):
    projet = Projet.objects.all()
    # resultat = '--'.join(
    #     p.nom_projet for p in projet
    # )
    # return HttpResponse(resultat)
    return render(request, 'App/affiche.html', {'pp': projet})



class Affiche(ListView):
    model = Projet
    template_name = 'App/affiche.html'
    context_object_name = 'pp'

def ajouter(request):
    if request.method == "GET":
        form = form = AddProjectForm()
        return render(request,'App/ajouter.html',{'f':form})


    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            result = form.save()
            result.save()
            return HttpResponseRedirect(reverse('liste'))
        else:
            return render(request,'App/ajouter.html',{'f':form,'msg_error':'could not add project'})


class ajouterP(CreateView):
    model = Projet
    fields = ('nom_projet','duree_projet','temps_alloue_par_projet',
                  'besoins','est_valide','createur')

    success_url = reverse_lazy('liste')
    # template_name = ""

def delete(request,id):
    # request.POST['id']
    projet = Projet.objects.get(pk = id)
    projet.delete()
    return HttpResponseRedirect(reverse('liste'))

class deleteP(DeleteView):
    model = Projet
    success_url = reverse_lazy('liste')


def update(request,id):


