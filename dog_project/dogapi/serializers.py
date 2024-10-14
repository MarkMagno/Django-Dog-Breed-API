from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds'] ##All Fields for Breeds

class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy'] ##All fields for dog

    def create(self, validated_data):
        breed_data = validated_data.pop('breed')
        breed = Breed.objects.create(**breed_data)
        dog = Dog.objects.create(breed=breed, **validated_data)
        return dog


    ##Generated using AI
    def update(self, instance, validated_data):
        breed_data = validated_data.pop('breed')
        breed = instance.breed

        # Update breed fields
        breed.name = breed_data.get('name', breed.name)
        breed.size = breed_data.get('size', breed.size)
        breed.friendliness = breed_data.get('friendliness', breed.friendliness)
        breed.trainability = breed_data.get('trainability', breed.trainability)
        breed.sheddingamount = breed_data.get('sheddingamount', breed.sheddingamount)
        breed.exerciseneeds = breed_data.get('exerciseneeds', breed.exerciseneeds)
        breed.save()

        # Update dog fields
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()

        return instance
