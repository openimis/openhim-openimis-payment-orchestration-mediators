from django.shortcuts import render
import json # this library facilitates loading of mediatorConfig.json

"""
The the upstreame server urls for openhim, openimis and python mediators 
For more information on this file, contact  developer Stephen Mburu
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import http.client

# This seriializer uses the configs model 
from .models import configs
from .serializers import configsSerializer

"""
This method to restrict serializer to only one instance. The function calls
mediators_save_configurations to save default configuration into database
"""
def configview():
	try: # attempt opening the default config json file from hidden conf directory
		data_dict = json.loads(open('.conf/mediatorsConfig.json').read())
		mediators_save_configurations(data_dict[0]) # call save configurations method
	except (FileNotFoundError,IOError) as e: # else bypass import and use django admin
		pass
	config = configs.objects.first()
	serializer = configsSerializer(config, many = False)
	config_data = serializer.data
	return Response(config_data)

"""
This method receives first array of the python dictionary and saves them as default 
mediator configuration values in the configs database table as requested by Patrick
"""
def mediators_save_configurations(json_configs): 
	config = None
	config = configs()
	for k,v in json_configs.items():
		setattr(config, k, v)
	config.save()
	return json_configs