from django import forms

from .models import Car, Concern, Showroom


class ModelNewCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['brand', 'engine', 'year', 'color', 'concern', 'showroom']


class FormNewCarForm(forms.Form):
    CHOICES = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('газ', 'газ'),
        ('гибрид', 'гибрид'),
    )
    brand = forms.CharField(max_length=25)
    engine = forms.ChoiceField(choices=CHOICES)
    year = forms.IntegerField()
    color = forms.CharField(max_length=15)
    concern = forms.ModelChoiceField(queryset=Concern.objects.all())
    showroom = forms.ModelMultipleChoiceField(queryset=Showroom.objects.all())


