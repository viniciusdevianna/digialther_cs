# Generated by Django 4.2 on 2023-04-26 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tamers', '0004_technique_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='character',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='character',
            name='body',
        ),
        migrations.RemoveField(
            model_name='character',
            name='defense',
        ),
        migrations.RemoveField(
            model_name='character',
            name='evasion',
        ),
        migrations.RemoveField(
            model_name='character',
            name='focus',
        ),
        migrations.RemoveField(
            model_name='character',
            name='mind',
        ),
        migrations.RemoveField(
            model_name='character',
            name='nature',
        ),
        migrations.RemoveField(
            model_name='character',
            name='resist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='social',
        ),
        migrations.RemoveField(
            model_name='character',
            name='spirit',
        ),
        migrations.AddField(
            model_name='attribute',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tamers.character'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stat',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tamers.character'),
            preserve_default=False,
        ),
    ]
