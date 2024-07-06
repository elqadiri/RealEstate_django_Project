from django.contrib import admin
from .models import Listings,ContactMessage , ListingImage 


# Register your models here.

class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1

class ListingsAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]

admin.site.register(Listings, ListingsAdmin)
admin.site.register(ListingImage)
admin.site.register(ContactMessage)

