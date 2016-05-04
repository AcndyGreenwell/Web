from django.contrib import admin

# Register your models here.

from .models import *
from guardian.admin import GuardedModelAdmin


class CameraAdmin(GuardedModelAdmin):
    # TODO реальзовать добавления permission на кнопку save в админке
    pass

admin.site.register(Camera, CameraAdmin)
admin.site.register(Zone)
admin.site.register(ZoneOption)
admin.site.register(Direction)
admin.site.register(OptionsSet)
admin.site.register(TimeTable)
admin.site.register(CUser)
admin.site.register(Company)
admin.site.register(Results)