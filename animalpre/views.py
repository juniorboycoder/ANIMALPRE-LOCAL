#import libraries
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from .forms import AnimalfeaturesForm,UserForm, MyAuthForm, AnimalfeaturesForm2,ContactForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import Animalfeatures
from . serializers import AnimalfeaturesSerializers
import pickle

import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
from django.contrib.auth.forms import AuthenticationForm
from sklearn.preprocessing import MinMaxScaler

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .token_generator import account_activation_token

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from newsapi import NewsApiClient

import requests

from django.db.models import Q
import random

import time


import datetime


# Create your views here.

#Index view for all visiting users
def HomeView(request):

 if request.method == 'GET':
	 form = ContactForm()
 #feedback form
 else:
	 form = ContactForm(request.POST)

	 if form.is_valid():
			messages.success(request,'thanks for your feedback')
			Your_email = ('animalpreuser@gmail.com')

			message = form.cleaned_data['message']
			to_email=  ('juniorboyboy2@gmail.com')
			
			email = EmailMessage(Your_email, message, to=[to_email])
			email.send()
			
			
 form=ContactForm()
 mydict={'form': form}
 return render(request, 'animalpre/index.html',context=mydict)


#Function to call a random animal from the API

def Randomanimal():
 
	movie_list = ['snake wildlife','Beetle', 'cat', 'dog', 'elephant', 'goat and cow','mammals','amphibians', 'leopard','antelop', 'monkeys','dolphins',
	'antelope','boar','buffalo','calf','cheetah','chicken','crab','crayfish','crow','deer','dove','duck','flamingo','frog','giraffe','hawk','honeybee',
	'housefly','mole','mongoose','moth','newt','octopus','opossum','oryx','ostrich','parakeet','penguin','piranha','pitviper','pony','porpoise','raccoon','reindeer','rhea',
	'Cockroach','Ant','Wolf','Dingo','Discus','Donkey','Electric Eel','Squirrel','Hamster','Honey Bee','Jaguar','Jackal','Grizzly Bear','Komodo Dragon'
	
	]

	moview_item = random.choice(movie_list)


	return moview_item

#News index view for signed up user

@ login_required
def HomeNewsView(request):
		#API Call from news API
		newsapi = NewsApiClient(api_key=" db9eb44b252446f594380d0a9b35efe0")

		#User search
		if request.method == 'GET':
			query= request.GET.get('q')
			
			try:
				if query is not None:

					topheadlines = newsapi.get_everything(qintitle=query )
					articles = topheadlines['articles']
					desc = []
					news = []
					img = []
					published=[]
					
					url=[]
				
					for i in range(len(articles)):
						myarticles = articles[i]
				
						news.append(myarticles['title'])
						desc.append(myarticles['description'])
						img.append(myarticles['urlToImage'])
						

						date_str = myarticles['publishedAt']

						date_str3= list(date_str)

						del date_str3[10:20]


						date_str4=''.join(date_str3)

						

						date_str2= str(date_str4)

						

						print(date_str2)

						format_str = '%Y-%m-%d' 

						publishedd = datetime.datetime.strptime(date_str2, format_str)

						published.append(publishedd)

						
						url.append(myarticles['url'])

				
				
					mylist = zip(news, desc, img, published,url)

					return render(request, 'animalpre/animalnewsfeed.html', context={"mylist":mylist})
					
			except:
					

					return render(request, 'animalpre/animalnewsfeed.html') 
			
			
			#Animal get displayed to user from animal function above into the news api if user do not search

			else:
				url = 'https://newsapi.org/v2/everything?'


				
				

				animal = Randomanimal()
				print(animal)
				newsapi = NewsApiClient(api_key=" db9eb44b252446f594380d0a9b35efe0")
				topheadlines = newsapi.get_everything(qintitle=animal,   language='en')
				articles = topheadlines['articles']

				desc = []
				news = []
				img = []
				published=[]
				contents=[]
				url=[]

				#Displaying API details in template
				for i in range(len(articles)):
					myarticles = articles[i]
			
					news.append(myarticles['title'])
					desc.append(myarticles['description'])
					img.append(myarticles['urlToImage'])

				
					date_str = myarticles['publishedAt']

					date_str3= list(date_str)

					del date_str3[10:20]


					date_str4=''.join(date_str3)

					

					date_str2= str(date_str4)

					

					print(date_str2)

					format_str = '%Y-%m-%d' 

					publishedd = datetime.datetime.strptime(date_str2, format_str)

					published.append(publishedd)

					
					url.append(myarticles['url'])

			
			
				mylist = zip(news, desc, img, published,url)

				return render(request, 'animalpre/animalnewsfeed.html',context={"mylist":mylist})
		else:
		
			

			return render(request, 'animalpre/animalnewsfeed.html',context={"mylist":mylist})


#Serializing the animal features model to be stored as an api
class AnimalfeaturesView(viewsets.ModelViewSet):
	queryset = Animalfeatures.objects.all()

	
	serializer_class = AnimalfeaturesSerializers





def prediction(unit):

	#LOAD SAVED TRAINED MODEL FROM LOCAL COMPUTER
	try:
		mdl=joblib.load("/Users/admin/Desktop/1.TOTORIAL/animalpre_model2.pkl")
		scalers=MinMaxScaler()
		X=unit.to_numpy()

		print (X)
		y_pred=mdl.predict(X)
		
		
		
		newdf=pd.DataFrame(y_pred, columns=['class_type'])

		newdf= newdf.replace({1:'Mammal', 2:'Bird',3:'reptile',4:'Fish',5:'Amphibian',6:'Bug',7:'Invertebrate'})
		
  
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])
 

#Prediction form for visiting users     
def FormViews(request):
	if request.method=='POST' and 'btnform1' in request.POST:
		form=AnimalfeaturesForm(request.POST)
		
		if form.is_valid() :
			

				predictedform = form.save(commit=False)
				
				

				

				does_it_have_hair = form.cleaned_data['does_it_have_hair']

				does_it_have_feathers= form.cleaned_data['does_it_have_feathers']

				does_it_lay_eggs = form.cleaned_data['does_it_lay_eggs']

				does_it_produce_milk = form.cleaned_data['does_it_produce_milk']
				
				is_it_airborne = form.cleaned_data['is_it_airborne']

				Is_it_Aquatic = form.cleaned_data['Is_it_Aquatic']

				is_it_a_predator = form.cleaned_data['is_it_a_predator']

				
				does_it_have_teeth = form.cleaned_data['does_it_have_teeth']

				does_it_have_backbone= form.cleaned_data['does_it_have_backbone']

				does_it_breath = form.cleaned_data['does_it_breath']

				is_it_venomous = form.cleaned_data['is_it_venomous']

				does_it_have_fins = form.cleaned_data['does_it_have_fins']
				
				how_many_legs = form.cleaned_data['how_many_legs']

				how_many_tails = form.cleaned_data['how_many_tails']

				is_it_domestic = form.cleaned_data['is_it_domestic']

				
				myDict = (request.POST).dict()

				print(myDict)


				
				df=pd.DataFrame(myDict, index=[0])

				#After collecting Data from user
				#Encode each variable yes and No As 1's and 0's for machine learning model
				

				df=df.drop("csrfmiddlewaretoken", axis=1)

				df= df.drop("btnform1", axis=1)

				df.does_it_have_hair[df.does_it_have_hair == 'Yes'] = '1'
				df.does_it_have_hair[df.does_it_have_hair == 'No'] = '0'

				df.does_it_have_feathers[df.does_it_have_feathers == 'Yes'] = '1'
				df.does_it_have_feathers[df.does_it_have_feathers == 'No'] = '0'

				df.does_it_lay_eggs[df.does_it_lay_eggs == 'Yes'] = '1'
				df.does_it_lay_eggs[df.does_it_lay_eggs == 'No'] = '0'

				df.does_it_produce_milk[df.does_it_produce_milk == 'Yes'] = '1'
				df.does_it_produce_milk[df.does_it_produce_milk== 'No'] = '0'

				df.is_it_airborne[df.is_it_airborne == 'Yes'] = '1'
				df.is_it_airborne[df.is_it_airborne == 'No'] = '0'

				df.Is_it_Aquatic[df.Is_it_Aquatic == 'Yes'] = '1'
				df.Is_it_Aquatic[df.Is_it_Aquatic == 'No'] = '0'

				df.is_it_a_predator[df.is_it_a_predator == 'Yes'] = '1'
				df.is_it_a_predator[df.is_it_a_predator == 'No'] = '0'

				df.does_it_have_teeth[df.does_it_have_teeth == 'Yes'] = '1'
				df.does_it_have_teeth[df.does_it_have_teeth == 'No'] = '0'

				df.does_it_have_backbone[df.does_it_have_backbone == 'Yes'] = '1'
				df.does_it_have_backbone[df.does_it_have_backbone == 'No'] = '0'

				df.does_it_breath[df.does_it_breath == 'Yes'] = '1'
				df.does_it_breath[df.does_it_breath == 'No'] = '0'

				df.is_it_venomous[df.is_it_venomous == 'Yes'] = '1'
				df.is_it_venomous[df.is_it_venomous == 'No'] = '0'

				df.does_it_have_fins[df.does_it_have_fins == 'Yes'] = '1'
				df.does_it_have_fins[df.does_it_have_fins == 'No'] = '0'

				df.is_it_domestic[df.is_it_domestic == 'Yes'] = '1'
				df.is_it_domestic[df.is_it_domestic == 'No'] = '0'

				
				print (df)

				#call the prediction function
				answer=prediction(df)[0]
				
				#Print messages after submitting the forma and prediction
				messages.success(request,'Animal class predicted: {}'.format(answer))

				b=format(answer)
				print (b)

				predictedform.predicted= b

				predictedform.save()





				
		
	form=AnimalfeaturesForm()

		#feedback after prediction

	if request.method=='POST' and 'btnform2' in request.POST:
		form=AnimalfeaturesForm3(request.POST)


		if form.is_valid() :
				predictedform = form.save(commit=False)
				
				

					
				
				


				predictedform = Animalfeatures.objects.latest('no')

				is_prediction_correct = form.cleaned_data['is_prediction_correct']

				predictedform.is_prediction_correct= is_prediction_correct

				what_animal_were_you_thinking_of = form.cleaned_data['what_animal_were_you_thinking_of']

				predictedform.what_animal_were_you_thinking_of= what_animal_were_you_thinking_of
				
				predictedform.save(update_fields=['what_animal_were_you_thinking_of', 'is_prediction_correct'])

	


				print ("i love you")

				return redirect('animalpre:apistuff')


	form=AnimalfeaturesForm()

	return render(request, 'animalpre/form.html', {'form':form})


#after register function
def thanksregister(request):
    
    return render(request, 'animalpre/thankyouregister.html')

#API list of prediction
def apistuff(request):

	api= Animalfeatures.objects.all()
    
	mydict={'api':api}
	
	return render(request, 'animalpre/api.html',context=mydict)

#Detail of each prediction
def apianimaldetail(request,pk=None):

    animalpostsdetail = get_object_or_404(Animalfeatures, pk=pk)
    
   
   
    return render(request, 'animalpre/animalapicontents.html', {'animalpostsdetail':animalpostsdetail})


##API list of prediction for logged in users
@ login_required
def apistuff2(request):

	api=Animalfeatures.objects.all()
    
	mydict={'api':api}
	
	return render(request, 'animalpre/api2.html',context=mydict)



#Activate account email message

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('animalpre:successregister')
    else:
        return HttpResponse('Activation link is invalid!')


def successregister(request):
    
    return render(request, 'animalpre/registrationsucess.html')


#login class

class LoginView(FormView):
	
    template_name = 'animalpre/login.html'
    form_class = MyAuthForm
    success_url = reverse_lazy('animalpre:newsfeed')


    def form_valid(self, form):
		
		
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
#signup
def usersignup(request):
				if request.method=='POST':
					form=UserForm(request.POST)
					if form.is_valid():		
							user = form.save(commit=False)
							user.is_active = False
							user.save()

							current_site = get_current_site(request)
							email_subject = 'Activate Your Account'
							message = render_to_string('animalpre/activate_account.html', {
								'user': user,
								'domain': current_site.domain,
								'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
								'token': account_activation_token.make_token(user),
							})
							to_email = form.cleaned_data.get('email')
							email = EmailMessage(email_subject, message, to=[to_email])
							email.send()

						
						
							user.save()
							
							
							return redirect('animalpre:thanksforreg')
				else:
							form = UserForm()
				return render(request, 'animalpre/signup.html',  {'form': form})

#logout user
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    
    return render(request, 'animalpre/logout_user.html',context)

#user profile
@ login_required  
def view_profile(request, pk=None):

 

 if pk:
         user = User.objects.get(pk=pk)
         
    
 else:
         
         user = request.user
 args = {'user': user}
 return render(request, 'animalpre/user_profile.html', args)




#Animal prediction form after user sign up, same as before
def FormViews2(request):
	if request.method=='POST' and 'btnform1' in request.POST:
		form=AnimalfeaturesForm(request.POST)
		
		if form.is_valid() :
			

				predictedform = form.save(commit=False)
				
				

				

				does_it_have_hair = form.cleaned_data['does_it_have_hair']

				does_it_have_feathers= form.cleaned_data['does_it_have_feathers']

				does_it_lay_eggs = form.cleaned_data['does_it_lay_eggs']

				does_it_produce_milk = form.cleaned_data['does_it_produce_milk']
				
				is_it_airborne = form.cleaned_data['is_it_airborne']

				Is_it_Aquatic = form.cleaned_data['Is_it_Aquatic']

				is_it_a_predator = form.cleaned_data['is_it_a_predator']

				
				does_it_have_teeth = form.cleaned_data['does_it_have_teeth']

				does_it_have_backbone= form.cleaned_data['does_it_have_backbone']

				does_it_breath = form.cleaned_data['does_it_breath']

				is_it_venomous = form.cleaned_data['is_it_venomous']

				does_it_have_fins = form.cleaned_data['does_it_have_fins']
				
				how_many_legs = form.cleaned_data['how_many_legs']

				how_many_tails = form.cleaned_data['how_many_tails']

				is_it_domestic = form.cleaned_data['is_it_domestic']

				
				myDict = (request.POST).dict()

				print(myDict)


				
				df=pd.DataFrame(myDict, index=[0])

				
				

				df=df.drop("csrfmiddlewaretoken", axis=1)

				df= df.drop("btnform1", axis=1)

				df.does_it_have_hair[df.does_it_have_hair == 'Yes'] = '1'
				df.does_it_have_hair[df.does_it_have_hair == 'No'] = '0'

				df.does_it_have_feathers[df.does_it_have_feathers == 'Yes'] = '1'
				df.does_it_have_feathers[df.does_it_have_feathers == 'No'] = '0'

				df.does_it_lay_eggs[df.does_it_lay_eggs == 'Yes'] = '1'
				df.does_it_lay_eggs[df.does_it_lay_eggs == 'No'] = '0'

				df.does_it_produce_milk[df.does_it_produce_milk == 'Yes'] = '1'
				df.does_it_produce_milk[df.does_it_produce_milk== 'No'] = '0'

				df.is_it_airborne[df.is_it_airborne == 'Yes'] = '1'
				df.is_it_airborne[df.is_it_airborne == 'No'] = '0'

				df.Is_it_Aquatic[df.Is_it_Aquatic == 'Yes'] = '1'
				df.Is_it_Aquatic[df.Is_it_Aquatic == 'No'] = '0'

				df.is_it_a_predator[df.is_it_a_predator == 'Yes'] = '1'
				df.is_it_a_predator[df.is_it_a_predator == 'No'] = '0'

				df.does_it_have_teeth[df.does_it_have_teeth == 'Yes'] = '1'
				df.does_it_have_teeth[df.does_it_have_teeth == 'No'] = '0'

				df.does_it_have_backbone[df.does_it_have_backbone == 'Yes'] = '1'
				df.does_it_have_backbone[df.does_it_have_backbone == 'No'] = '0'

				df.does_it_breath[df.does_it_breath == 'Yes'] = '1'
				df.does_it_breath[df.does_it_breath == 'No'] = '0'

				df.is_it_venomous[df.is_it_venomous == 'Yes'] = '1'
				df.is_it_venomous[df.is_it_venomous == 'No'] = '0'

				df.does_it_have_fins[df.does_it_have_fins == 'Yes'] = '1'
				df.does_it_have_fins[df.does_it_have_fins == 'No'] = '0'

				df.is_it_domestic[df.is_it_domestic == 'Yes'] = '1'
				df.is_it_domestic[df.is_it_domestic == 'No'] = '0'

				
				print (df)


				answer= prediction(df)[0]
				
				
				messages.success(request,'Animal class predicted: {}'.format(answer))

				b=format(answer)
				print (b)

				predictedform.predicted= b

				predictedform.save()





				
		
	form=AnimalfeaturesForm()

	if request.method=='POST' and 'btnform2' in request.POST:
		form=AnimalfeaturesForm3(request.POST)


		if form.is_valid() :
				predictedform = form.save(commit=False)
				
				

					
				
				


				predictedform = Animalfeatures.objects.latest('no')

				is_prediction_correct = form.cleaned_data['is_prediction_correct']

				predictedform.is_prediction_correct= is_prediction_correct

				what_animal_were_you_thinking_of = form.cleaned_data['what_animal_were_you_thinking_of']

				predictedform.what_animal_were_you_thinking_of= what_animal_were_you_thinking_of
				
				predictedform.save(update_fields=['what_animal_were_you_thinking_of', 'is_prediction_correct'])

	


				print ("i love you")

				return redirect('animalpre:apistuff2')


	form=AnimalfeaturesForm()

	return render(request, 'animalpre/predictform.html', {'form':form})

