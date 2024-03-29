# Generated by Django 4.2 on 2023-04-21 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tamers', '0002_aspiration_attribute_digimon_stat_technique_path_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EvolutionForms',
            new_name='EvolutionForm',
        ),
        migrations.CreateModel(
            name='AvailableTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.character')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamers.technique')),
            ],
        ),
    ]
