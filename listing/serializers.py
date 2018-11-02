from rest_framework import serializers
from .models import Categories, Listing, Asset
# from rest_framework.authtoken.models import Token




#API_Serializer_Here

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
