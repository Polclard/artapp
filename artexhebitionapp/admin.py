from django.contrib import admin

from artexhebitionapp.models import Exhibition, Artist, Art


# Register your models here.

class ArtAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class ArtistAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return True

class ExhibitionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return True


admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)