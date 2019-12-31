from django import forms

from eica.models import Personas


class PersonasForm(forms.ModelForm):

    class Meta:
        model = Personas
        fields = ['nombre', 
                  'edad', 
                  'dni', 
                #   'fecha_creado',
                   ]
        labels = {'nombre': "NombreX",
                  'edad': "EdadX",
                  'dni': "DniX",
                #   'fecha_creado': "FechaCreadoX",
                  }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'x'}),
            'edad': forms.TextInput(attrs={'class':'x'}),
            'dni': forms.TextInput(attrs={'class':'x'}),
            # 'fecha_creado': forms.DateTimeField(),
            }
