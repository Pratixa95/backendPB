# from django.contrib import admin

# # Register your models here.

# from .models import ContactMessage

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ("full_name", "email", "created_at")
#     search_fields = ("full_name", "email")


from django.contrib import admin
from .models import Portfolio, GalleryImage, ContactMessage


# --------------------- #
#  GALLERY IMAGES INLINE
# --------------------- #
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    fields = ("image", )
    readonly_fields = ()
    show_change_link = True


# -------------------------- #
#   MAIN PORTFOLIO ADMIN
# -------------------------- #
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "phone", "created_at")
    search_fields = ("name", "mail", "phone")
    list_filter = ("created_at",)

    fields = (
        "name",
        "bio",
        "mail",
        "phone",
        "address",
        "logo",
        "profile_pic",
    )

    inlines = [GalleryImageInline]


# -------------------------- #
#    CONTACT MESSAGE ADMIN
# -------------------------- #
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "created_at")
    search_fields = ("full_name", "email")
    list_filter = ("created_at",)


# OPTIONAL:
# If you want Gallery Images to also appear as main menu
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "portfolio", "image")
    search_fields = ("portfolio__name",)
