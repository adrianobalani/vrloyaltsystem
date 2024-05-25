from django import forms
from .models import Sale, SaleDetail, Customer, Seller


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(forms.ModelForm):

    class Meta:
        model = SaleDetail
        fields = '__all__'

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'
        
class SellerForm(forms.ModelForm):
    
    class Meta:
        model = Seller
        fields = '__all__'        
