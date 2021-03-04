from django.contrib import admin

# Register your models here.
from .models import Phone
from .models import Trademark

admin.site.register(Phone)
admin.site.register(Trademark)
