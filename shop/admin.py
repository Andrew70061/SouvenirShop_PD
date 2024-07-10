from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from shop.models import Product, ProductCategory, ProductImages, Supplier, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class SupplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)

class ProductImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductImages, ProductImagesAdmin)

class ProductAdminInline(admin.TabularInline):
    model = ProductImages
    extra = 0

class ProductCategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'sale_price', 'quantity', 'publish', 'created', 'updated']
    list_filter = ['publish', 'created']
    list_editable = ['quantity', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductAdminInline]

admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

#Фильтр по статусам заказов
class StatusFilter(admin.SimpleListFilter):
    title = 'Статус заказа'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return Order.STATUS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

#Заказы и поиск по заказам
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated', StatusFilter]
    search_fields = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

#Добавление модели User
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.site_header = 'Администратирование Souvenir Shop'
