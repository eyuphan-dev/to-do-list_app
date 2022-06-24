from django.contrib import admin
from .models import Todos

# Register your models here.

#models de yaptıklarımızı admin sayfasına ekleme
admin.site.register(Todos)