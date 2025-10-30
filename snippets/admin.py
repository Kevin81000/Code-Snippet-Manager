# project/snippets/admin.py
from django.contrib import admin
from .models import Snippet

# Register the Snippet model
admin.site.register(Snippet)


