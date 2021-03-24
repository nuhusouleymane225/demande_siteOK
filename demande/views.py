from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from demande.forms import DemandeForm
from demande.models import Demande


# Create your views here.
@login_required
def home_view(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def faire_demande(request):
    form = DemandeForm(request.POST or None)
    if form.is_valid():
        obj = Demande.objects.create(** form.cleaned_data)
        obj.save()
        form = DemandeForm
        print('data valid')
    else:
        print('data is not valid')
    context = {'form': form}
    template_name = 'demande1.html'
    return render(request, template_name, context)
