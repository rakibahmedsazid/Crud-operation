from django.contrib import admin
from myApp.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id',"name",'roll','address','img']
    
admin.site.register(Students,StudentAdmin)
