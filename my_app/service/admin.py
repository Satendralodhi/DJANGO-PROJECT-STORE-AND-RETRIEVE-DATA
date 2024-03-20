from django.contrib import admin
from service.models import services
class serviceA(admin.ModelAdmin):
    list_display=('name','contactnumber','email','address','image')
admin.site.register(services,serviceA)
# Register your models here.
