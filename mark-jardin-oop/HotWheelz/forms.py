from django import forms
from .models import CarBrand, CarModel, Collection, Owner

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']
        
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'description', 'image']
        
class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'cars']
        
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'collection']