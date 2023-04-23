from django.urls import path, include
from . import views
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('players', views.PlayersViewSet, basename='players')
router.register('digimon', views.DigimonViewSet, basename='digimon')
router.register('evolution', views.EvolutionFormsViewSet, basename='evolution')
router.register('characters', views.CharactersViewSet, basename='characters')
router.register('techniques', views.TechniquesViewSet, basename='techniques')

urlpatterns = [
    path('', include(router.urls)),
    path('aspirations/', views.ListAspirations.as_view()),
    path('paths/', views.ListPaths.as_view()),
    path('paths/aspiration/<int:pk>/', views.ListPathsAspiration.as_view()),
    path('evolution/digimon/<int:pk>/', views.ListEvolutionFormBaseForm.as_view()),
    path('evolution/stage/<int:pk>/', views.ListEvolutionFormStage.as_view()),
    path('player/characters/<int:pk>/', views.ListCharacterPlayer.as_view()),
    path('character/<int:pk>/evolution/', views.AvailableFormViewSet.as_view({'get': 'list'}), name='available_forms'),
    path('character/<int:pk>/tech/', views.AvailableTechniqueViewSet.as_view({'get': 'list'}), name='available_tech'),
]