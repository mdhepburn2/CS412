# File: admin.py
# Author: Matthew Hepburn, 9/24/2026
# Description: register the models for use by admin

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)