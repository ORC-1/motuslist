from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import *
# from django.contrib.auth import authenticate
from .serializers import *


# DEF VIEW SYNTAX

# class PollList(APIView):
#     def get(self, request):
#         results = Listing.objects.all()[:20]
#         data = SearchSerializer(results, many=True ).data
#
#         return Response(data)



class SearchResult(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SearchSerializer
