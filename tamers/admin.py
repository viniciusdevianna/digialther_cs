from django.contrib import admin
from django.apps import apps
from .models import *

admin.site.register(apps.all_models['tamers'].values())
