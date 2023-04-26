from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class Player(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class Aspiration(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Path(models.Model):
    aspiration = models.ForeignKey(Aspiration, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    intrinsic = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Technique(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    cooldown = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Digimon(models.Model):

    class ColorGroup(models.TextChoices):
        RED = 'R', _('Vermelho')
        PURPLE = 'P', _('Roxo')
        YELLOW = 'Y', _('Amarelo')
        BLUE = 'B', _('Azul')
        GREEN = 'G', _('Verde')
        BLACK = 'L', _('Preto')

    name = models.CharField(max_length=50)
    aspiration = models.ForeignKey(Aspiration, on_delete=models.SET_NULL, null=True)
    path = models.ForeignKey(Path, on_delete=models.SET_NULL, null=True)
    group = models.CharField(max_length=1, choices=ColorGroup.choices)    
    tech = models.ForeignKey(Technique, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class EvolutionForm(models.Model):
    
    class EvolutionStages(models.IntegerChoices):
        BABY = 0, _('Baby')
        ROOKIE = 1, _('Rookie')
        CHAMPION = 2, _('Champion')
        ULTIMATE = 3, _('Ultimate')
        MEGA = 4, _('Mega')
        ULTRA = 5, _('Ultra')

    name = models.CharField(max_length=50)
    base_form = models.ForeignKey(Digimon, on_delete=models.CASCADE)
    stage = models.IntegerField(choices=EvolutionStages.choices)
    condition = models.CharField(max_length=400, blank=True, default="")
    tech = models.ForeignKey(Technique, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Character(models.Model):

    class Race(models.TextChoices):
        ALTALIA = 'ALT', _("Altalia")
        FENÍRIO = 'FEN', _("Fenírio")
        GOLLYCK = 'GOL', _("Gollyck")
        LODGER = 'LOD', _("Lodger")
        MAEK = 'MAE', _("Maek")
        NUAA = 'NUA', _("Nuaa")
        PAISHU = 'PAI', _("Paishu")
        QUADIR = 'QUA', _("Qua'dir")
        RAE = 'RAE', _("Rae")
        SAITYR = 'SAI', _("Saityr")


    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    race = models.CharField(max_length=3, choices=Race.choices)
    origin = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    height = models.DecimalField(decimal_places=2, max_digits=3)
    inventory = models.CharField(max_length=1000, blank=True)
    annotations = models.CharField(max_length=1000, blank=True)

    digimon = models.ForeignKey(Digimon, on_delete=models.SET_NULL, null=True)

    level = models.PositiveIntegerField()
    current_xp = models.PositiveIntegerField(default=0)
    total_xp = models.PositiveIntegerField(default=0)
    pd = models.PositiveIntegerField(default=0)

    total_lp = models.IntegerField(default=0)
    current_lp = models.IntegerField(default=0)
    temp_lp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def update_total_xp(self, xp_value):
        if self.total_xp + xp_value < 0 or self.current_xp + xp_value < 0:
            raise ValueError('A experiência não pode ter valor menor que zero')
        else:
            self.total_xp += xp_value
            self.current_xp += xp_value

    def spend_experience(self, xp_value):
        if xp_value < 0:
            if self.current_xp - xp_value > self.total_xp:
                raise ValueError('Não é possível ganhar experiência acima da sua experiência total')
        if self.current_xp - xp_value < 0:
            raise ValueError('Você não tem experiência suficiente para esta operação')
        else:
            self.current_xp -= xp_value

    def get_attributes(self):
        attributes = Attribute.objects.filter(character=self.pk)
        if not attributes:
            raise ValueError('Não há atributos criados para essa personagem')
        return {attribute.category.label: attribute for attribute in attributes}
    
    def get_stats(self):
        stats = Stat.objects.filter(character=self.pk)
        if not stats:
            raise ValueError('Não há stats criados para essa personagem')
        return {stat.category.label: stat for stat in stats}

class Attribute(models.Model):

    class Category(models.TextChoices):
        BODY = 'C', _('Corpo')
        MIND = 'M', _('Mente')
        FOCUS = 'F', _('Foco')
        SPIRIT = 'E', _('Espírito')
        SOCIAL = 'S', _('Social')
        NATURE = 'N', _('Natureza')

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=Category.choices)
    current_value = models.PositiveIntegerField(default=0)
    total_value = models.PositiveIntegerField(default=0)
    training_level = models.IntegerField(default=0)

    def __str__(self):
        return self.category

class Stat(models.Model):

    class Category(models.TextChoices):
        DEFENSE = 'D', _('Defesa')
        RESIST = 'R', _('Resistência')
        BALANCE = 'B', _('Equilíbrio')
        ACCURACY = 'A', _('Acerto')
        EVASION = 'E', _('Esquiva')

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=Category.choices)
    total_value = models.IntegerField(default=0)
    current_value = models.IntegerField(default=0)
    dice = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.category

class AvailableForm(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    evolution_form = models.ForeignKey(EvolutionForm, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.evolution_form.name
    
class AvailableTechnique(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    tech = models.ForeignKey(Technique, on_delete=models.CASCADE)
