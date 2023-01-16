from django.contrib import admin
from django.apps import AppConfig
from .models import(Inkoranya,Ubukwe,Imbyino,Ibikoresho,Ubuhinzi,Indamukanyo,
Amasano,Ikibonezamvugo,Umurage,Hugura)

class Core_advertConfig(AppConfig):
    name='core_advert'

class InkoranyaAdmin(admin.ModelAdmin):
    list_display='name'

class UbukweAdmin(admin.ModelAdmin):
    list_display='name'

class ImbyinoAdmin(admin.ModelAdmin):
    list_display='name'

class IbikoreshoAdmin(admin.ModelAdmin):
    list_display='name'

class UbuhinziAdmin(admin.ModelAdmin):
    list_display='name'

class IndamukanyoAdmin(admin.ModelAdmin):
    list_display='name'

class AmasanoAdmin(admin.ModelAdmin):
    list_display='name'

class IkibonezamvugoAdmin(admin.ModelAdmin):
    list_display='name'

class UmurageAdmin(admin.ModelAdmin):
    list_display='name'

class HuguraAdmin(admin.ModelAdmin):
    list_display='name'


admin.site.register(Inkoranya)
admin.site.register(Ubukwe)
admin.site.register(Imbyino)
admin.site.register(Ibikoresho)
admin.site.register(Ubuhinzi)
admin.site.register(Indamukanyo)
admin.site.register(Amasano)
admin.site.register(Ikibonezamvugo)
admin.site.register(Umurage)
admin.site.register(Hugura)
