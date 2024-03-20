from django.contrib import admin

# Register your models here.

from service.models import service
class serviceAd(admin.ModelAdmin):
    list_display=('name','contactnumber','email','taskname','mark')
admin.site.register(service,serviceAd)