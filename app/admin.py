from django.contrib import admin

# Register your models here.
from .models import Contact, Projet, Certifications, Experience, Technology, Cv, Formation, ProjetImage

class ProjetImageInline(admin.TabularInline):
    model = ProjetImage
    extra = 1

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    inlines = [ProjetImageInline]
    list_display = ('name', 'date_created')

admin.site.register(Certifications)
admin.site.register(Experience)
admin.site.register(Technology)
admin.site.register(Contact)
admin.site.register(Cv)
admin.site.register(Formation)