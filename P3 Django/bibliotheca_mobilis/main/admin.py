from django.contrib import admin
from main.models import chaosAspectVenerated, creationRace, creationSide, creationType

# Register your models here.
admin.site.register(chaosAspectVenerated)
admin.site.register(creationRace)
admin.site.register(creationSide)
admin.site.register(creationType)