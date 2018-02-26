from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from bootstrap_datepicker.widgets import DatePicker

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user =super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        widgets = {
            'date_of_birht': forms.DateTimeInput(attrs={'class': 'datepicker'})
        }
        model = UserProfile
        exclude = ['']

