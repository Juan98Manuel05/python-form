from django import forms
from .models import Requests

class RequestForm( forms.ModelForm ):

    class Meta:
        model = Requests
        fields = ('date_hour_attention','date_hour_attention_finish','company','city','affair','response')
        labels = {
            'date_hour_attention': 'fecha y hora de atencion: (dd/mm/yyyy HH:mm:ss)',
            'date_hour_attention_finish': 'fecha y hora de atencion final: (dd/mm/yyyy HH:mm:ss)',
            'company': 'Empresa',
            'city': 'Ciudad',
            'affair': 'Asunto',
            'response': 'Respuesta',
        }

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = "Seleccione la ciudad"
        self.fields['response'].required = False
        self.fields['date_hour_attention'].required = True
        self.fields['date_hour_attention_finish'].required = True

    def dateInvalid(self):
        date1 = self.cleaned_data.get['date_hour_attention']
        if date1 == '':
            raise forms.ValidationError('Fecha incorrecta')