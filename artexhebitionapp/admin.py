import datetime

from django.contrib import admin
from django.utils import timezone

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

    def get_queryset(self, request):
        # Return only the arts that the currently logged-in User has made
        qs = super().get_queryset(request)
        return qs.filter(artist__user=request.user).distinct()

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
    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        return hasattr(request.user, 'arts')

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return hasattr(request.user, 'arts')

    def get_queryset(self, request):
        # By default, it retrieves all objects for the model (Exhibition in this case) unless further filtering is applied.
        current_logged_in_artist = Artist.objects.filter(user=request.user).first()
        all_artist_arts = Art.objects.filter(artist=current_logged_in_artist).distinct()
        ret_list = []
        for art in all_artist_arts:
            ret_list.append(art.exhibition.id)
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            time_now = timezone.now()
            return qs.filter(start_date__lte=time_now, end_date__gte=time_now)
        elif hasattr(request.user, 'arts'):
            return qs.filter(id__in=ret_list).distinct()

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)


admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
