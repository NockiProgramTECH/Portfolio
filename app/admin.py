from django.contrib import admin

# Register your models here.
from .models import Contact, Projet, Certifications, Experience, Technology,Cv

admin.site.register(Projet)
admin.site.register(Certifications)
admin.site.register(Experience)
admin.site.register(Technology)
admin.site.register(Contact)
admin.site.register(Cv)