from rest_framework import serializers
from .models import Dog, Breed


##Taken from dogapp labs
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['TINY', 'SMALL', 'MEDIUM', 'LARGE']

class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(), source='breed', write_only=True
    )

    ##Taken fromi dogapp labs
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']