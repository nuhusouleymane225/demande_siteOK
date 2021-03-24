from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    """ 
        l'utilisateur 
    """
    code_matricule = models.CharField(max_length=10, default="")
    code_nom = models.CharField(max_length=50, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction_service = models.CharField(max_length=70, default="")
    is_actif = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now_add=True)
    date_entre = models.DateField(blank=True, null=True)
    code_service = models.CharField(max_length=5)
    ville = models.CharField(max_length=80)

    def __str__(self):
        return self.code_nom


class Chauffeur(models.Model):
    chauffeur_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=90)
    code_mat = models.CharField(max_length=8, default="")
    ville = models.CharField(max_length=80, default="")
    date_creation = models.DateField(auto_now_add=True)
    date_entre = models.DateField(blank=True, null=True)
    est_actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code_mat} - {self.nom}"




class Motif(models.Model):
    motif_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200, default="")
    date_creation = models.DateField(auto_now_add=True)
    date_modif = models.DateField(auto_now_add=True)
    prix_unitaire = models.FloatField()
    def __str__(self):
        return self.libelle

class Demande(models.Model):
    demande_id = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ('attente', 'ATTENTE'),
        ('valide', 'VALIDE'),
        ('annule', 'ANNULE'),
    )
    axeAnalyseChoix = [
        ('200', 'Batiment et charge locative'),
        ('210', 'Voyage & deplacement'),
        ('220', 'Fourniture & consommable de bureau'),
        ('230', 'Charge personnel'),
        ('240', 'Quote-part depreciation immo'),
        ('250', 'Personnel & services exterieur'),
        ('260', 'Relation exterieur'),
        ('270', 'Impôt & taxes'),
        ('280', 'Autres charges directions et service'),
        ('900', "Recette d'exploitation"),
        ('910', 'Frais/Opération (frais voyages)'),
        ('920', 'Papier administratif-CR'),
        ('930', "Main d'oevre dédiée"),
        ('940', 'Quote-part amortissement CR et autres'),
        ('950', 'Entretien & reparation CR'),
        ('960', 'Frais generaux'),
        
        
    ]

    directionActChoix = [
        ('DGE', 'Dir. Générale'),
        ('DCF', 'Dir. Financière'),
        ('DRH', 'Dir. RH'),
        ('DEX', 'Dir. Exploitation'),
        ('DET', 'Dir. Technique'),
        ('DCM', 'Dir. Commerciale'),
        ('SMG', 'Moyens Generaux'),
        ('FHY', 'fret Hydrocarbure'),
        ('FSB', 'fret boisson'),
        ('FHP', 'fret huile de palm'),
        ('FTC', 'fret conteneurs'),
        ('FCS', 'fret canne à sucre'),
        ('FDI', 'fret divers'),
        ('LEV', 'levage'),
        ('LOC', 'location de surfaces'),
        ('SDI', 'services divers'),
        ('RAV', 'revenus à ventiler'),
        ('PAF', 'Prestation Accessoir'),
        ('COL', 'fret Colis lourds'),
        
    ]

    



    agenceeChoix = [
        ('0000', 'Siège'),
        ('0001', 'Abidjan (agence principale)'),
        ('0002', 'Bouaflé'),
        ('0003', 'San-Pedro'),
        ('0007', 'Bouaké'),
        ('0008', 'Yamoussoukro'),
        ('0009', 'Ferké'),
        ('0010', 'Minautores'),
        
        
    ]



    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='attente')
    # element permettant la description
    demande_item = models.TextField(null=True, verbose_name="Observation")
    nom_demandeur = models.ForeignKey(User, on_delete=models.CASCADE)
    num_releve = models.CharField(max_length=255, null=True, verbose_name="Numéro de relevé")
    cod_mat_chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE, null=True, verbose_name="Chauffeur")
    cod_vehicule = models.CharField(max_length=255, default="", null=True, verbose_name="Code véhicule")
    code_remorque = models.CharField(max_length=255, default="", null=True, verbose_name="Code remorque")
    imat_vehicule = models.CharField(max_length=255, default="", null=True, verbose_name="Imat. véhicule")
    imat_remorque = models.CharField(max_length=255, default="", null=True, verbose_name="Imat. remorque")
    motif = models.ForeignKey(Motif, on_delete=models.CASCADE,verbose_name="Motif", null=True)
    date_frais = models.DateField(blank=True, null=True, verbose_name='Date de frais')
    date_demande = models.DateField(auto_now_add=True, null=True)
    prix_total = models.FloatField(blank=True, null=True)
    agence = models.CharField(max_length=255, choices=agenceeChoix, verbose_name='Code Agence')
    activite = models.CharField(max_length=255, choices=directionActChoix, verbose_name='Code Activité')
    analyse = models.CharField(max_length=255, choices=axeAnalyseChoix, verbose_name='Code Analyse')
    quantite = models.IntegerField(default=0)
    urgenceChoix = [
        ('A Exécuter Immediatement','A Exécuter Immediatement'),
        ('A Exécuter Dans Les Plus Brefs Délais', 'A Exécuter Dans Les Plus Brefs Délais'),
        ('Peut Etre Reporté', 'Peut Etre Reporté'),
    ]
    urgence = models.CharField(max_length=255, choices=urgenceChoix, verbose_name='Urgence')

    def __str__(self):
        return f"{self.num_releve} - {self.status}"