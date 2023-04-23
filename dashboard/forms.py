
from django import forms
from .models import  product


   


class add_product(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'product_name',
            'weight',
            'PROcategory',
            'prices',
            'description',
            'PROimg',
            ]   
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'أسم المنتج'}), 
            'weight': forms.NumberInput(attrs={'class':'form-control','placeholder': 'الوزن'}),  
            'PROcategory': forms.Select(attrs={'class':'form-control','placeholder': 'نوع المنتج'}),  
            'prices': forms.NumberInput(attrs={'class':'form-control','placeholder': 'السعر'}),  
            'description': forms.TextInput(attrs={'class':'form-control','placeholder': 'وصف المنتج'}),   
            'PROimg': forms.FileInput(attrs={'class':'form-control'}),
        }
    


        
      
      
    