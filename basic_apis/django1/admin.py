from django.contrib import admin

# Register your models here.
from .models import user,Person,address,Employee,Customer

class Add(admin.ModelAdmin):
    list_display=['name','rollno']

admin.site.register(user)
admin.site.register(Person,Add)
admin.site.register(address)
admin.site.register(Customer)


admin.site.register(Employee)

