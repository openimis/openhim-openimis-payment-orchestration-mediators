from django.db.utils import OperationalError
from patient_mediator.views import getClient
from patient_mediator.views import registerClientMediator

from group_mediator.views import getGroup
from group_mediator.views import registerGroupMediator

from organization_mediator.views import getOrganization
from organization_mediator.views import registerOrganizationMediator

from invoice_mediator.views import getInvoice
from invoice_mediator.views import registerInvoiceMediator
""" 
Register Mediators - once -- uncomment after setting up variables
The function throws invalid Url; to check after setting variables
"""
try:
    registerClientMediator()
except OperationalError:
    pass  # when db tables do not exist yet load the app without this side effect

try:
    registerGroupMediator()
except OperationalError:
    pass  # when db tables do not exist yet load the app without this side effect

try:
    registerOrganizationMediator()
except OperationalError:
    pass  # when db tables do not exist yet load the app without this side effect

try:
    registerInvoiceMediator()
except OperationalError:
    pass  # when db tables do not exist yet load the app without this side effect