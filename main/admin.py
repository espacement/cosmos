from django.contrib import admin
from main.models import plots
from .models import Order, OrderItem
# Register your models here.
admin.site.register(plots)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['plot']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_cost', 'created_at']
    list_filter = ['created_at']
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)