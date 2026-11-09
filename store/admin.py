# store/admin.py
from django.contrib import admin
from .models import Category, Product
from .models import Order, OrderItem
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Automatically writes out the slug as you type the name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available'] # Lets you change prices rapidly directly inside lists
    prepopulated_fields = {'slug': ('name',)}

# store/admin.py (Append to the end)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'paid', 'created']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
