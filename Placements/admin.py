from django.contrib import admin
from .models import Companies

# Register your models here.






admin.site.register(Companies)
admin.site.site_header = "Placements Admin"
admin.site.site_title = "Placements Admin Portal"

