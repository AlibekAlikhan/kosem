from django.contrib import admin

from webapp.models import Photo


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "photo")
    list_filter = ("id", "photo")
    search_fields = ("photo", )
    filter = ("photo",)
    readonly_fields = ("id",)


admin.site.register(Photo, ImageAdmin)
