from django.contrib import admin

# Register your models here.
from .models import Profile , Phones , Address
# from django.contrib.auth.models import User

# Register your models here.

# class MyUser(UserAdmin):
#     pass





class PhonesAdmin(admin.TabularInline):
    model = Phones

class AddressAdmin(admin.TabularInline):
    model = Address


class ProfileAdmin(admin.ModelAdmin):
    # inlines = [PhonesAdmin,AddressAdmin]
    pass




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Phones)
admin.site.register(Address)