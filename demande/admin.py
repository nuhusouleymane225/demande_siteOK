from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Utilisateur, Chauffeur, Motif, Demande
# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Chauffeur)
admin.site.register(Motif)
admin.site.register(Demande)

admin.site.site_header = "SUIVI DES FRAIS D'EXPLOITATION"
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    #pour avoir un deroulant basé sur l'heure
    date_hierarchy = 'action_time'

    #filtrer le resultat par utilisateur
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # permettre la recherche dans obj_repr et dans change_message

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    
    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"