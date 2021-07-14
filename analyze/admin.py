from django.contrib import admin
from .models import User
# Register your models here.
admin.site.site_title = 'Breast Cancer Detection'
admin.site.site_header = 'Breast Cancer Detection'
admin.site.index_title = 'Breast Cancer Detection'
admin.site.register(User)