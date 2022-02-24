
from django.contrib import admin, messages

from .models import Etudiant, Coach, Projet, MemberShipInProject


# Register your models here.

class MemberShip(admin.TabularInline):
    model = MemberShipInProject
    extra = 1
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    inlines = (MemberShip,)
    list_display = (
        'nom_projet', 'duree_projet', 'temps_alloue_par_projet', 'est_valide', 'createur', 'besoins', 'description',
        'superviseur')
    fieldsets = (('A propos', {'fields': ('nom_projet', 'besoins', 'description')}),
                 ('Etat', {'fields': ('est_valide',)}),
                 ('Duree', {'fields': ('duree_projet', 'temps_alloue_par_projet')}),
                 (None, {'fields': ('createur', 'superviseur')})
                 )
    list_per_page = 2

    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)

    def set_to_false(self, request, queryset):
        row_no_valid = queryset.filter(est_valide=False)
        if row_no_valid.count() > 0:
            messages.error(request, "%s This Articles are already invalid" % row_no_valid.count())
        else:
            a = queryset.update(est_valide=False)
            if a != 0:
                messages.success(request, "% s project was updated " %a)

    set_to_valid.short_description = 'Validate'
    set_to_false.short_description = 'Blocked'

    actions = ['set_to_valid', 'set_to_false']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ('est_valide','createur')
    search_fields = ['nom_projet']
admin.site.register(Etudiant)
admin.site.register(Coach)
# admin.site.register(Projet,ProjetAdmin)
