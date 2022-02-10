from django.db.utils import OperationalError
from patient_mediator.views import getClient
from patient_mediator.views import registerClientMediator

""" 
Register Mediators - once -- uncomment after setting up variables
The function throws invalid Url; to check after setting variables
"""
try:
    registerClientMediator()
except OperationalError:
    pass  # when db tables do not exist yet load the app without this side effect