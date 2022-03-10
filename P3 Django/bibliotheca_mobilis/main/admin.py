from django.contrib import admin
from community.models import chaosAspectVenerated, creationRace, creationSide, specialities

# Register your models here.
admin.site.register(chaosAspectVenerated)
admin.site.register(creationRace)
admin.site.register(creationSide)
admin.site.register(specialities)