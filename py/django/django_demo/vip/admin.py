from django.contrib import admin
from vip.models import VIPUser
from vip.models import Bill


class BillInline(admin.TabularInline):
    model = Bill
    extra = 1
    
    
class VIPUserAmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'bluetooth_addr', 'balance', 'scores')
    search_fields = ['phone']
    inlines = [BillInline]
    
    
class BillAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'item', 'num', 'unit', 'price', 'total']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]


admin.site.register(VIPUser, VIPUserAmin)
admin.site.register(Bill, BillAdmin)

admin.AdminSite.site_header = '知了'
admin.AdminSite.site_title = '知了管理'
