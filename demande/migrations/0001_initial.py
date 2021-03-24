# Generated by Django 3.1.7 on 2021-03-24 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('chauffeur_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=90)),
                ('code_mat', models.CharField(default='', max_length=8)),
                ('ville', models.CharField(default='', max_length=80)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_entre', models.DateField(blank=True, null=True)),
                ('est_actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motif',
            fields=[
                ('motif_id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(default='', max_length=200)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_modif', models.DateField(auto_now_add=True)),
                ('prix_unitaire', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_matricule', models.CharField(default='', max_length=10)),
                ('code_nom', models.CharField(default='', max_length=50)),
                ('direction_service', models.CharField(default='', max_length=70)),
                ('is_actif', models.BooleanField(default=True)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_entre', models.DateField(blank=True, null=True)),
                ('code_service', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=80)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('demande_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('attente', 'ATTENTE'), ('valide', 'VALIDE'), ('annule', 'ANNULE')], default='attente', max_length=255)),
                ('demande_item', models.TextField(null=True, verbose_name='description')),
                ('num_releve', models.CharField(max_length=255, null=True)),
                ('cod_vehicule', models.CharField(default='', max_length=255, null=True)),
                ('code_remorque', models.CharField(default='', max_length=255, null=True)),
                ('imat_vehicule', models.CharField(default='', max_length=255, null=True)),
                ('imat_remorque', models.CharField(default='', max_length=255, null=True)),
                ('prix_total', models.CharField(default='', max_length=255, null=True)),
                ('date_frais', models.CharField(default='', max_length=255, null=True)),
                ('agence', models.CharField(choices=[('0000', 'Siège'), ('0001', 'Abidjan (agence principale)'), ('0002', 'Bouaflé'), ('0003', 'San-Pedro'), ('0007', 'Bouaké'), ('0008', 'Yamoussoukro'), ('0009', 'Ferké'), ('0010', 'Minautores')], max_length=255, verbose_name='Agence')),
                ('activite', models.CharField(choices=[('DGE', 'Dir. Générale'), ('DCF', 'Dir. Financière'), ('DRH', 'Dir. RH'), ('DEX', 'Dir. Exploitation'), ('DET', 'Dir. Technique'), ('DCM', 'Dir. Commerciale'), ('SMG', 'Moyens Generaux'), ('FHY', 'fret Hydrocarbure'), ('FSB', 'fret boisson'), ('FHP', 'fret huile de palm'), ('FTC', 'fret conteneurs'), ('FCS', 'fret canne à sucre'), ('FDI', 'fret divers'), ('LEV', 'levage'), ('LOC', 'location de surfaces'), ('SDI', 'services divers'), ('RAV', 'revenus à ventiler'), ('PAF', 'Prestation Accessoir'), ('COL', 'fret Colis lourds')], max_length=255, verbose_name='Activité')),
                ('analyse', models.CharField(choices=[('200', 'Batiment et charge locative'), ('210', 'Voyage & deplacement'), ('220', 'Fourniture & consommable de bureau'), ('230', 'Charge personnel'), ('240', 'Quote-part depreciation immo'), ('250', 'Personnel & services exterieur'), ('260', 'Relation exterieur'), ('270', 'Impôt & taxes'), ('280', 'Autres charges directions et service'), ('900', "Recette d'exploitation"), ('910', 'Frais/Opération (frais voyages)'), ('920', 'Papier administratif-CR'), ('930', "Main d'oevre dédiée"), ('940', 'Quote-part amortissement CR et autres'), ('950', 'Entretien & reparation CR'), ('960', 'Frais generaux')], max_length=255, verbose_name='Analyse')),
                ('urgence', models.CharField(choices=[('A Exécuter Immediatement', 'A Exécuter Immediatement'), ('A Exécuter Dans Les Plus Brefs Délais', 'A Exécuter Dans Les Plus Brefs Délais'), ('Peut Etre Reporté', 'Peut Etre Reporté')], max_length=255, verbose_name='Urgence')),
                ('cod_mat_chauffeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demande.chauffeur')),
                ('nom_demandeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demande.utilisateur')),
            ],
        ),
    ]