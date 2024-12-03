from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField(required=False)  # Поле для загрузки фото

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Шифрование пароля
        if commit:
            user.save()
            # Проверяем, если фото загружено, то устанавливаем его в профиль
            if 'photo' in self.cleaned_data and self.cleaned_data['photo']:
                user.profile.set_photo(self.cleaned_data['photo'])
                user.profile.save()  # Сохраняем профиль с обновленным фото
        return user
