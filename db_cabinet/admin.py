from django.contrib import admin
from .models import Patient
from .models import Rendez_Vou




@admin.register(Rendez_Vou)
class Rendez_VouAdmin(admin.ModelAdmin):
    list_display = ('Date','patient')
    # search_fields = ('patient.full_name',)
    list_filter = ('Date',)
    ordering = ('Date',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'publish', 'phone')
    list_filter = ('publish',)
    search_fields = ('full_name', 'description', 'slug', 'phone')
    prepopulated_fields = {'slug': ('full_name',)}
    date_hierarchy = 'publish'
    ordering = ('-publish',)

