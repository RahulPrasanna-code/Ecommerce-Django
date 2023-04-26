from django.forms import ModelForm,Form
from products.models import Product

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name','image_url','description','price','category',
            'label','available_quantity','rating'
        ]
        exclude = ['seller']

class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name','image_url','description','price','category',
            'label','available_quantity','rating'
        ]