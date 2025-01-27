from django.contrib import admin

from artexhebitionapp.models import Exhibition, Artist, Art


# Register your models here.

class ArtAdmin(admin.ModelAdmin):
    readonly_fields = ('artist',)
    def has_module_permission(self, request):
        return hasattr(request.user, 'arts')

    def has_add_permission(self, request):
        return hasattr(request.user, 'arts')

    def has_change_permission(self, request, obj=None):
        return hasattr(request.user, 'arts')

    def has_delete_permission(self, request, obj=None):
        return hasattr(request.user, 'arts')

    def has_view_permission(self, request, obj=None):
        return hasattr(request.user, 'arts')

    def save_model(self, request, obj, form, change):
        found_artist = Artist.objects.filter(user=request.user).first()
        obj.artist = found_artist
        super().save_model(request, obj, form, change)


class ArtistAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)


class ExhibitionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)


admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
