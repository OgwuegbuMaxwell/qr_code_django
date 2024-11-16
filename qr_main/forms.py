from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50, 
        label='Restaurant Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Restaurant Name'
        })
        
    )
    url = forms.URLField(
        max_length=200, 
        label='Menu Url',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the Url'
        })
    )
    


