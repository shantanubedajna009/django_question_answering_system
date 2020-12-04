from django.contrib import admin
from qsapp.models import Answers, Questions

# Registering the Models 
# to use them with Admin panel
admin.site.register(Answers)
admin.site.register(Questions)
