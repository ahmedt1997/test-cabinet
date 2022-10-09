from django.db import models
from django.utils import timezone


class Patient(models.Model):

    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')

    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.full_name


class Rendez_Vou(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ('Date',)
    def __str__(self):
        return self.patient.full_name