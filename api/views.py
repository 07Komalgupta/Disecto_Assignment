from django.db.models import manager
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import item
from .serializers import itemSerializer
from rest_framework.decorators import api_view
from json import *
import json

import requests


@api_view(['GET'])
def apiOverview(request):
    apiurls= {
        'Show Item List' : 'itemlist/',
        'Show Particular Item\'s Details' : "itemdetail/itemid/",
        'Add Item' : 'itemadd/',
        'Particular Item Update' : 'itemupdate/itemid/',
        'Item Delete ' : 'itemdelete/itemid/',
        'Download Pdf' : 'download/'
    }

    return Response(apiurls)

@api_view(['GET'])
def itemList(request):
    items = item.objects.all()
    serializer = itemSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def itemDetail(request,pk):
    items = item.objects.get(id=pk)
    serializer = itemSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
    serializer = itemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request,pk):
    items = item.objects.get(id=pk)
    serializer = itemSerializer(instance= items, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def itemDelete(request,pk):
    items = item.objects.get(id=pk)
    items.delete()
    return Response("Item Deleted Successfully !!")



def download(request):
    items = item.objects.all()
    print(items[2])
    sum = 0
    for i in items:
        print(i.name)
        total = (i.qnt * i.price)
        sum = sum +total
        print(total)
    print("Total : ", sum)
    return render(request, 'list.html',{'res': items, 'total': sum})




# class itemList(APIView):

# def get(self, request):
#     item1 = item.objects.all()
#     serializer = itemSerializer(item1, many=True)
#     return Response(serializer.data)

# def post(self):
#     pass
