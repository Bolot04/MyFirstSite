from django import forms

from users.models import Profile


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    password2 = password
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError("Не правильный пароль!")
        else:
            del cleaned_data['password2']
            return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=8)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'bio', 'profile_pic']