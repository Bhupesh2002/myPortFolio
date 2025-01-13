from django.contrib import admin
from .models import HealthData

admin.site.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    list_display = ('age', 'weight', 'exercise', 'duration', 'calories_burned')
    search_fields = ('age','exercise')