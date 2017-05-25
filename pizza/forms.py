from django.contrib.auth.models import User#importar el modelo de usuario en este formulario
from django import forms #importamos la librería de forms, que nos facilita crear un formulario de html

class UserForm(forms.ModelForm): #creamos user form y heredamos las caracteríaticas de modelForm
    password = forms.CharField(widget=forms.PasswordInput) # usamos la columna password de html, aquí decimos que no muestre los caracteres y que los oculte

    class Meta: #eta es para mapear la información, no tiene
        model = User #coge el modelo de user para tener la información de este modelo
        fields = ['username', 'email', 'password'] #y lo personalizamos con estos tres campos