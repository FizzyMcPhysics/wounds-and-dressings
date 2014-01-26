from django.contrib import admin

from .models import Wound, Dressing, WoundType

admin.site.register(Wound)
admin.site.register(WoundType)
admin.site.register(Dressing)