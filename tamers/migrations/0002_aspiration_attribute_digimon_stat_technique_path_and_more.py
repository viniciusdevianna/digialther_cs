# Generated by Django 4.2 on 2023-04-20 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tamers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('C', 'Corpo'), ('M', 'Mente'), ('F', 'Foco'), ('E', 'Espírito'), ('S', 'Social'), ('N', 'Natureza')], max_length=1)),
                ('current_value', models.PositiveIntegerField(default=0)),
                ('total_value', models.PositiveIntegerField(default=0)),
                ('training_level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Digimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(choices=[('R', 'Vermelho'), ('P', 'Roxo'), ('Y', 'Amarelo'), ('B', 'Azul'), ('G', 'Verde'), ('L', 'Preto')], max_length=1)),
                ('aspiration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamers.aspiration')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('D', 'Defesa'), ('R', 'Resistência'), ('B', 'Equilíbrio'), ('A', 'Acerto'), ('E', 'Esquiva')], max_length=1)),
                ('total_value', models.IntegerField(default=0)),
                ('current_value', models.IntegerField(default=0)),
                ('dice', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('cooldown', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('intrinsic', models.CharField(max_length=400)),
                ('aspiration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.aspiration')),
            ],
        ),
        migrations.CreateModel(
            name='EvolutionForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stage', models.IntegerField(choices=[(0, 'Baby'), (1, 'Rookie'), (2, 'Champion'), (3, 'Ultimate'), (4, 'Mega'), (5, 'Ultra')])),
                ('condition', models.CharField(blank=True, default='', max_length=400)),
                ('base_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.digimon')),
                ('tech', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamers.technique')),
            ],
        ),
        migrations.AddField(
            model_name='digimon',
            name='path',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamers.path'),
        ),
        migrations.AddField(
            model_name='digimon',
            name='tech',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamers.technique'),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('race', models.CharField(choices=[('ALT', 'Altalia'), ('FEN', 'Fenírio'), ('GOL', 'Gollyck'), ('LOD', 'Lodger'), ('MAE', 'Maek'), ('NUA', 'Nuaa'), ('PAI', 'Paishu'), ('QUA', "Qua'dir"), ('RAE', 'Rae'), ('SAI', 'Saityr')], max_length=3)),
                ('origin', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('inventory', models.CharField(max_length=1000)),
                ('annotations', models.CharField(max_length=1000)),
                ('level', models.PositiveIntegerField()),
                ('current_xp', models.PositiveIntegerField(default=0)),
                ('total_xp', models.PositiveIntegerField(default=0)),
                ('pd', models.PositiveIntegerField(default=0)),
                ('total_lp', models.IntegerField(default=0)),
                ('current_lp', models.IntegerField(default=0)),
                ('temp_lp', models.IntegerField(default=0)),
                ('accuracy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.stat')),
                ('balance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.stat')),
                ('body', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
                ('defense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.stat')),
                ('digimon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamers.digimon')),
                ('evasion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.stat')),
                ('focus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
                ('mind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
                ('nature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('resist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.stat')),
                ('social', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
                ('spirit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamers.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.character')),
                ('evolution_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.evolutionforms')),
            ],
        ),
    ]