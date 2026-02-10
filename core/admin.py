from django.contrib import admin
from .models import Customer, Deal, Note

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('name', 'email', 'phone')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'amount', 'created_by', 'created_at')
    list_filter = ('status', 'created_by', 'created_at')
    search_fields = ('title', 'customer__name')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_by', 'created_at', 'short_content')
    list_filter = ('created_by', 'created_at')
    search_fields = ('content', 'customer__name')

    def short_content(self, obj):
        return obj.content[:50]
