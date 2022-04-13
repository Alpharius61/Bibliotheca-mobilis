from django.contrib import admin
from community.models import chaosAspectVenerated, races, Side, speciality
# Register your models here.
admin.site.register(chaosAspectVenerated)
admin.site.register(races)
admin.site.register(Side)
admin.site.register(speciality)