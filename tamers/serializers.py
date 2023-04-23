from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'email']

class ListAspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspiration
        fields = ['id', 'name']

class ListPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ['id', 'name', 'aspiration', 'intrinsic']

class ListPathAspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ['id', 'name', 'intrinsic']

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'category', 'current_value', 'total_value', 'training_level']

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'category', 'current_value', 'total_value', 'dice']

class TechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technique
        fields = ['id', 'name', 'description', 'cooldown']

class DigimonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digimon
        fields = ['id', 'name', 'aspiration', 'path', 'group', 'tech']

class EvolutionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionForm
        fields = ['id', 'name', 'stage', 'base_form', 'condition', 'tech']

class ListEvolutionFormBaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionForm
        fields = ['id', 'name', 'stage', 'condition', 'tech']

class ListEvolutionFormStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionForm
        fields = ['id', 'name', 'stage', 'condition', 'tech']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id',
            'name',
            'player',
            'race',
            'origin',
            'age',
            'weight',
            'height',
            'inventory',
            'annotations',
            'digimon',
            'level',
            'current_xp',
            'total_xp',
            'pd',
            'attributes',
            'current_lp',
            'total_lp',
            'temp_lp',
            'stats'
        ]

class ListCharacterPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'race', 'digimon']

class AvailableFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableForm
        fields = ['evolution_form', 'level']

class AvailableTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTechnique
        fields = ['tech']
