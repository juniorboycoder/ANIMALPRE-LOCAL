from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Animalfeatures
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput





class ContactForm(forms.Form):

    

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your feedback after using app'
        }
    ))
    
    
   

class AnimalfeaturesForm2(forms.Form):
	
	
	
	does_it_have_hair=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No'),('', '----')])
	
	does_it_have_feathers=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No'),('', '----')])

	does_it_lay_eggs=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	does_it_produce_milk=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	is_it_airborne=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	Is_it_Aquatic=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	is_it_a_predator=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	does_it_have_teeth=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	does_it_have_backbone=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	does_it_breath=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	is_it_venomous=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])

	does_it_have_fins=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])
	
	how_many_legs_plus_hands=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of legs & hands'}))

	how_many_tails=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of tails'}))

	is_it_domestic=forms.ChoiceField(choices=[(1, 'Yes'),(0, 'No')])


class AnimalfeaturesForm(forms.ModelForm):

    
    class Meta:
      model  = Animalfeatures
     
      
      
      fields = [  'does_it_have_hair','does_it_have_feathers','does_it_lay_eggs','does_it_produce_milk','is_it_airborne','Is_it_Aquatic',
      'is_it_a_predator','does_it_have_teeth','does_it_have_backbone','does_it_breath','is_it_venomous','does_it_have_fins','how_many_legs','how_many_tails','is_it_domestic','predicted','is_prediction_correct','what_animal_were_you_thinking_of']
	
class  AnimalfeaturesForm3(forms.ModelForm):
    

    class Meta:


      model  = Animalfeatures
     
      
      
      fields = [ 'predicted','is_prediction_correct','what_animal_were_you_thinking_of']
	

class UserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username'
        }
    ))
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email'
        }
    ))
    
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))
    
    password2 = forms.CharField(widget=forms.TextInput (
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password again'
        }
    ))
    

    class Meta:

      model  = User
      fields = ['username','email','password1','password2']
      email =forms.EmailField(required = True)
    

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        
        except User.MultipleObjectsReturned:
             user = User.objects.filter(email=email).order_by('id')[0]

        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False