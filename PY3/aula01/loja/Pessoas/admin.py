from django.contrib import admin
from .models import Cliente
from .models import CPFCNPJ

# Register your models here.
admin.site.register(Cliente)
admin.site.register(CPFCNPJ)