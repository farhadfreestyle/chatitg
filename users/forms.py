from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import TextInput, PasswordInput


Users = get_user_model()




class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=5, max_length=30, widget=TextInput(attrs={
        'required':'true', 
        'type':'text', 
        'name':'logname', 
        'class':'form-style', 
        'placeholder':'Your First Name', 
        'id':'logname',
        'autocomplete':'off',

    }))
    last_name = forms.CharField(min_length=5, max_length=30, widget=TextInput(attrs={
        'required':'true', 
        'type':'text', 
        'name':'logname', 
        'class':'form-style', 
        'placeholder':'Your Last Name', 
        'id':'logname',
        'autocomplete':'off',

    }))
    email = forms.EmailField(required=True, widget=TextInput(attrs={
        'required':'true', 
        'type':'email', 
        'name':'logemail', 
        'class':'form-style', 
        'placeholder':'Your Email', 
        'id':'logemail',
        'autocomplete':'off',

    }))
    password1 = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(attrs={
        'required':'true', 
        'type':'password', 
        'name':'logpass', 
        'class':'form-style', 
        'placeholder':'Your Password', 
        'id':'logpass',
        'autocomplete':'off',

    }))
    password2 = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(attrs={
        'required':'true', 
        'type':'password', 
        'name':'logpass', 
        'class':'form-style', 
        'placeholder':'Your Password', 
        'id':'logpass',
        'autocomplete':'off',

    }))


    class Meta:
        model = Users
        fields = ('first_name','last_name', 'email', 'password1')




class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=TextInput(attrs={
        'required':'true', 
        'type':'email', 
        'name':'logemail', 
        'class':'form-style', 
        'placeholder':'Your Email', 
        'id':'logemail',
        'autocomplete':'off',
        

    }))
    password = forms.CharField( required=True, widget=TextInput(attrs={
        'required':'true', 
        'type':'password', 
        'name':'logpass', 
        'class':'form-style', 
        'placeholder':'Your Password', 
        'id':'logpass',
        'autocomplete':'off'

    }))



class ProfileForm(forms.ModelForm):

    profile_picture = forms.FileField(required=False,  widget=TextInput(attrs={
        
        'type':'file', 
        'class':'pic', 
        'id':'wizard-picture' ,
        
        

    }))

    first_name = forms.CharField(min_length=5, max_length=30, widget=TextInput(attrs={
        'required':'true', 
        'type':'text', 
        'name':'first-name', 
        'class':'input-text', 
        'placeholder':'Your First Name', 
        'id':'first-name',
        'autocomplete':'off',

       
    
        
    }))


    last_name = forms.CharField(min_length=5, max_length=30, widget=TextInput(attrs={
        'required':'true', 
        'type':'text', 
        'name':'last-name', 
        'class':'input-text', 
        'placeholder':'Your Last Name', 
        'id':'last-name',
        'autocomplete':'off'

    }))

    email = forms.CharField(min_length=5, max_length=300, widget=TextInput(attrs={
        'required':'true', 
        'type':'email', 
        'name':'your-email', 
        'class':'input-text', 
        'placeholder':'Your Email', 
        'id':'your-email',
        'autocomplete':'off',
        'readonly':'True'

    }))



    phone = forms.CharField(min_length=5, max_length=30, required=False,  widget=TextInput(attrs={
        'required':'true', 
        'type':'text', 
        'name':'phone', 
        'class':'input-text', 
        'placeholder':'Your Phone Number', 
        'id':'phone',
        'autocomplete':'off'

    }))


    class Meta:
        model = Users
        fields = ('first_name','last_name','phone', )