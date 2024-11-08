from rest_framework import serializers
from .models import SpyCat
import requests
from django.conf import settings


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']

    def validate_breed(self, value):
        # Проверяем породу через TheCatAPI
        url = 'https://api.thecatapi.com/v1/breeds'
        headers = {'x-api-key': settings.THE_CAT_BREED_API_KEY}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise serializers.ValidationError("Unable to validate breed at the moment.")

        breeds = {breed['name'] for breed in response.json()}
        if value not in breeds:
            raise serializers.ValidationError("Breed not recognized by TheCatAPI.")

        return value

class SpyCatSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['salary']