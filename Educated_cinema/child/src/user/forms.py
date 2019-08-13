from django import forms
from django.contrib.auth.models import User
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم', max_length=30, help_text='اسم المستخدم يجب ان لايحتوي على مسافات')
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password' != cd|'password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم')
        return cd['username']
