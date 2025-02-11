from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label="Nome de Usuário ou Email", max_length=254)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(email=username).first()
        if user is None:
            user = User.objects.filter(username=username).first()
        if user is None:
            raise forms.ValidationError("Usuário ou email inválido")
        self.cleaned_data['username'] = user.username
        return self.cleaned_data['username']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email