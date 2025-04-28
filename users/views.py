from django.shortcuts import render
from django.http import JsonResponse
from .models import Waitlist
from .serializers import WaitlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, filters

@api_view(['GET', 'POST'])
def waitlist(request, format=None):

    if request.method == 'GET':
        waitlist_entry = Waitlist.objects.all()
        serializer = WaitlistSerializer(waitlist_entry, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = WaitlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def list_detail(request, id, format=None):

    try:
        waitlist_entry = Waitlist.objects.get(pk=id)
    except Waitlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = WaitlistSerializer(waitlist_entry)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = WaitlistSerializer(waitlist_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        waitlist_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WaitlistListAPIView(generics.ListAPIView):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'dob']
    ordering_fields = ['dob']
    ordering = ['dob']

