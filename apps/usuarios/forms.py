from django.contrib.auth.forms import AuthenticationForm
from django import forms 
from apps.usuarios.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de un usuario en la base de datos

    """
    password1 = forms.CharField(label='Contaseña',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña ....',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label='Contaseña de Confirmación',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña ....',
            'id' : 'password2',
            'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = {'email','username','nombres','apellidos'}
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo Electronico',}),
            'nombres': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre',}),
            'apellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese sus apellidos',}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre de usuario',})
            
        }
