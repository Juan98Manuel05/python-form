from django import forms
from .models import customer, requests

class customerForm(forms.ModelForm):

    class Meta:
        model = customer
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. code'
        }

    
    def __init__(self, *args, **kwargs):
        super(customerForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False

class requestsForm(forms.ModelForm):

    class Meta:
        model = requests
        fields = {'date_hour_attention'}
        labels = {
            'date_hour_attention': 'Fecha y Hora Atencion'
        }