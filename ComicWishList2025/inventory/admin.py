from django.contrib import admin
from .models import Comic

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'grade', 'price')

