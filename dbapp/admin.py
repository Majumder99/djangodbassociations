from django.contrib import admin
from .models import Interest, City, Person, PersonAddress

# Define a custom admin for each model

class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile')

class PersonAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_person_name', 'city', 'street_address')
    
    def get_person_name(self, obj):
        return obj.person.name
    get_person_name.admin_order_field = 'person'  # Allows column order sorting
    get_person_name.short_description = 'Person Name'  # Renames column head

# Register your models and the corresponding admin class
admin.site.register(Interest, InterestAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonAddress, PersonAddressAdmin)
