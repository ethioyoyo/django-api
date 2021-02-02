from django.contrib import admin

# Register your models here.
from hostgenapp.models import hosts, MyUserProfile

admin.site.register(hosts)
admin.site.register(MyUserProfile)
