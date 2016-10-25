from django import forms
from member.models import MyUser
from django.contrib.auth import password_validation

class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = MyUser
        fields = (
            'email',
            'password1',
            'password2',
            'last_name',
            'first_name',
            'nickname',
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'})

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password1'],
            self.instance
        )
        return password2

    def save(self, commit=True):
        # return super(SignupModelForm, self).save(commit=commit)
        user = super(SignupModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class SignupForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    nickname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )