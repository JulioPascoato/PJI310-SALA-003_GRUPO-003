from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Professor, Habilidade


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'autofocus': 'autofocus'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class HabilidadeForm(ModelForm):
    class Meta:
        model = Habilidade
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(HabilidadeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
