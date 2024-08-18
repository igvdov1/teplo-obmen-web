from django.contrib import admin
from .models import TeploObmennik, ProductCard, Year
# Register your models here.
class TeploobmenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

# class TeploobmenAdmin2(admin.ModelAdmin):
#     list_display = ('date')
class ProductCardInline(admin.TabularInline):
    model = ProductCard
    extra = 1

class YearAdmin(admin.ModelAdmin):
    inlines = [ProductCardInline]

admin.site.register(Year, YearAdmin)
admin.site.register(ProductCard)
# admin.site.register(Date, TeploobmenAdmin2)
admin.site.register(TeploObmennik, TeploobmenAdmin)
