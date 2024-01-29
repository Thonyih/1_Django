from django.contrib import admin

# Register your models here.
from .models import Product #relative import because they are  in same dir

admin.site.register(Product)