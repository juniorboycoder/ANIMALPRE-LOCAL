from django.db import models

import django

from django.urls import reverse

# Create your models here.
class Animalfeatures(models.Model):
	
	

	does_it_have_feathers_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	is_it_airborne_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	is_it_a_predator_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	Is_it_Aquatic_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_have_teeth_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_breath_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_have_hair_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_lay_eggs_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_produce_milk_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)


	is_it_venomous_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_have_fins_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	does_it_have_backbone= (
		('Yes', 'Yes'),
		('No', 'No')
	)

	is_it_domestic_choice= (
		('Yes', 'Yes'),
		('No', 'No')
	)
	
	is_prediction_correct= (
		('Yes', 'Yes'),
		('No', 'No')
	)



	does_it_have_hair=models.CharField(max_length=15, choices=does_it_have_hair_choice, null=True)

	does_it_have_feathers=models.CharField(max_length=15, choices=does_it_have_feathers_choice, null=True)

	does_it_lay_eggs=models.CharField(max_length=15, choices=does_it_lay_eggs_choice, null=True)

	does_it_produce_milk=models.CharField(max_length=15, choices=does_it_produce_milk_choice, null=True)

	is_it_airborne=models.CharField(max_length=15, choices=is_it_airborne_choice, null=True)

	Is_it_Aquatic=models.CharField(max_length=15, choices=Is_it_Aquatic_choice, null=True)

	is_it_a_predator=models.CharField(max_length=15, choices=is_it_a_predator_choice, null=True)

	does_it_have_teeth=models.CharField(max_length=15, choices=does_it_have_teeth_choice, null=True)

	does_it_have_backbone=models.CharField(max_length=15, choices=does_it_have_backbone, null=True)

	does_it_breath=models.CharField(max_length=15, choices=does_it_breath_choice, null=True)

	is_it_venomous=models.CharField(max_length=15, choices=is_it_venomous_choice, null=True)

	does_it_have_fins=models.CharField(max_length=15, choices=does_it_have_fins_choice, null=True)

	how_many_legs=models.IntegerField(default=0, null=True)

	how_many_tails=models.IntegerField(default=0, null=True)
	
	is_it_domestic=models.CharField(max_length=15, choices=is_it_domestic_choice, null=True)

	predicted=models.CharField(max_length=15,  blank=True, null=True)
	
	is_prediction_correct=models.CharField (max_length=15,choices=is_prediction_correct,blank=True, null=True)

	what_animal_were_you_thinking_of=models.CharField(max_length=15,  blank=True, null=True)

	no=models.IntegerField(primary_key=True)

	

	def __str__(self):
		return str(self.no)

	
	def get_absolute_url(self):
		return reverse('animalpre:apidetail', kwargs={'pk': self.no})

	
	

	

	

	







	