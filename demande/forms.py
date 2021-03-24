from django.forms import ModelForm, RadioSelect, TextInput, DateInput, Select

from .models import Demande

class DemandeForm(ModelForm):
    class Meta:
        
        model = Demande
        exclude = ['demande_item', 'agence', 'analyse']
        widgets = {
            'urgence': Select,
            'date_frais': DateInput(attrs={'type':'date'}),
            'activite': Select
            
            
            
        }


class DemandeTraiteForm(ModelForm):
    class Meta:
        model = Demande
        exclude = ['demande_id']
        widgets={
            'status': RadioSelect,
            'analyse': RadioSelect,
            'agence': RadioSelect,
            'demande_item': TextInput
        }