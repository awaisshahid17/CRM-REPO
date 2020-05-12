from django.contrib import admin
from .models import Promocode,Calculator,Code


# Register your models here.

class PromocodeAdmin(admin.ModelAdmin):
    list_display =  ["code",'is_Available','is_free','PROMO_TYPE','AMOUNT','PERCENT','amount_percent']
    search_fields =  ["code",'is_Available','is_free','PROMO_TYPE','AMOUNT','PERCENT','amount_percent']


class CalculatorAdmin(admin.ModelAdmin):
    list_display =  ["firstnumber",'lastnumber','type','result','user']
    search_fields = ["firstnumber",'lastnumber','type','result','user']


class CodeAdmin(admin.ModelAdmin):
    list_display =  ["name",'email','phone','age','status']
    search_fields =  ["name",'email','phone','age','status']


admin.site.register(Calculator, CalculatorAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(Code, CodeAdmin)
