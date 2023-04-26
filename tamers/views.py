from rest_framework import viewsets, generics
from .serializers import *
from .models import *

class PlayersViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Player.objects.filter(is_active=True)
    
    serializer_class = PlayerSerializer

class ListAspirations(generics.ListAPIView):

    queryset = Aspiration.objects.all()
    serializer_class = ListAspirationSerializer

class ListPaths(generics.ListAPIView):

    queryset = Path.objects.all()
    serializer_class = ListPathSerializer

class ListPathsAspiration(generics.ListAPIView):
    def get_queryset(self):
        return Path.objects.filter(aspiration=self.kwargs['pk'])
    
    serializer_class = ListPathAspirationSerializer

class DigimonViewSet(viewsets.ModelViewSet):

    queryset = Digimon.objects.all()
    serializer_class = DigimonSerializer

class TechniquesViewSet(viewsets.ModelViewSet):

    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer

class EvolutionFormsViewSet(viewsets.ModelViewSet):

    queryset = EvolutionForm.objects.all()
    serializer_class = EvolutionFormSerializer

class ListEvolutionFormBaseForm(generics.ListAPIView):
    def get_queryset(self):
        return EvolutionForm.objects.filter(base_form=self.kwargs['pk'])
    
    serializer_class = ListEvolutionFormBaseFormSerializer

class ListEvolutionFormStage(generics.ListAPIView):
    def get_queryset(self):
        return EvolutionForm.objects.filter(stage=self.kwargs['pk'])
    
    serializer_class = ListEvolutionFormStageSerializer

class CharactersViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class ListCharacterPlayer(generics.ListAPIView):
    def get_queryset(self):
        return Character.objects.filter(player=self.kwargs['pk'])
    
    serializer_class = ListCharacterPlayerSerializer

class AttributesViewSet(viewsets.ModelViewSet):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class ListAttributesCharacter(generics.ListAPIView):
    def get_queryset(self):
        return Attribute.objects.filter(character=self.kwargs['pk'])
    
    serializer_class = ListAttributeCharacterSerializer

class StatsViewSet(viewsets.ModelViewSet):

    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class ListStatsCharacter(generics.ListAPIView):
    def get_queryset(self):
        return Stat.objects.filter(character=self.kwargs['pk'])
    
    serializer_class = ListStatCharacterSerializer

class AvailableFormViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return AvailableForm.objects.get(character=self.kwargs['pk'])
    
    def create(self, request, *args, **kwargs):
        character = Character.objects.get(self.kwargs['pk'])
        request.data['character'] = character
        return super.create(self, request, *args, **kwargs)
    
    serializer_class = AvailableFormSerializer

class AvailableTechniqueViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return AvailableTechnique.objects.get(character=self.kwargs['pk'])
    
    def create(self, request, *args, **kwargs):
        character = Character.objects.get(self.kwargs['pk'])
        request.data['character'] = character
        return super.create(self, request, *args, **kwargs)
    
    serializer_class = AvailableTechniqueSerializer
