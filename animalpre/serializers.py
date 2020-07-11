from rest_framework import serializers
from . models import Animalfeatures

class AnimalfeaturesSerializers(serializers.ModelSerializer):
	class Meta:
		model=Animalfeatures
		fields='__all__'

