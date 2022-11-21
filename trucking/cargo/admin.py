from django.contrib import admin
from .models import Request, Review



class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'date')
    list_filter = ('name', 'date')
    search_fields = ('name', 'email')

    date_hierarchy = 'date'
admin.site.register(Request, RequestAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('name', 'date')
    search_fields = ('name', 'email')
admin.site.register(Review, ReviewAdmin)
