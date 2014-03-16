from django.contrib import admin
from monitor.models import * 

# Register your models here.
class AssetAdmin(admin.ModelAdmin):
    '''manager Asset
    '''
    fields = [ 'asset_type', 'purchase_date', 'asset_name', \
            'asset_role', 'asset_content', ] 
    list_display = ['asset_id', 'asset_type', 'purchase_date', 'asset_name', \
            'asset_role', 'asset_content', ]
    def save_model(self, request, obj, form, change):
        if request.method == 'POST':
            ass_type = request.POST.get('asset_type', '')
            ass_name = request.POST.get('asset_name', '')
            ass_role = request.POST.get('asset_role', '')
            print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
            print ass_type
            print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        obj.asset_id = ass_type + "_" + ass_name + "_" + ass_role 
        obj.save()

class contactAdmin(admin.ModelAdmin):
    '''manager contact'''
    fieldsets = [
            ('Contact name', {'fields':['name'],'classes':'default'}),
            ('Contact Phone(optional)', {'fields':['number'],'classes':'collapse'}),
            ]



admin.site.register(asset, AssetAdmin)
admin.site.register(type)
admin.site.register(role)
admin.site.register(contact, contactAdmin)
