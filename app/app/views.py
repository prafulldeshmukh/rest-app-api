from django.shortcuts import render
import requests
from django.http import JsonResponse
import re

def getMacDetails(request,mac_address):
    
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
       url = "https://api.macaddress.io/v1?apiKey=at_4moXmufjfcGUN8rs08qIuZjcBfNQg&output=json"
       params = {'search': mac_address}
       data = requests.get(url,params=params).json()
       data = {	    
		"mac_address": mac_address,
		"companyName": data['vendorDetails']['companyName']
             }   
       return JsonResponse(data,safe=False)   
    else:
        return JsonResponse('You have eneterd invalid MAC Address',safe=False) 


