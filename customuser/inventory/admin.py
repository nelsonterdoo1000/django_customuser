# from django.contrib import admin
# from .models import Product
# from import_export.admin import ImportExportModelAdmin
# from .resources import ProductResource


# @admin.register(Product)
# class ProductAdmin(ImportExportModelAdmin):
#     resource_class = ProductResource
#     list_display = ['name','category','quantity']
#     search_fields = ['name','category']
    
#     # 
# # admin.site.register(Product,ProductAdmin)

from django.apps import apps
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

def create_dynammic_resource(model):
    class DynamicResource(resources.ModelResource):
        class Meta:
            model = model
            fields = [field.name for field in model._meta.get_fields()]
            export_order = fields
            exclude = ('password',) if 'password' in fields else ()
    return DynamicResource

app_config = apps.get_app_config('inventory')
all_models = app_config.get_models()

for model in all_models:
    try: 
        admin_class_attrs = {
            'resource_class':create_dynammic_resource(model),
            # 'list_display':[field.name for field in model._meta.get_fields()],
            'search_fields':[field.name for field in model._meta.get_fields()],
            'list_filter':[field.name for field in model._meta.get_fields()],
        }

        admin_class = type(f'{model.__name__}Admin',(ImportExportModelAdmin,),admin_class_attrs)

        if not admin.site.is_registered(model):
            admin.site.register(model,admin_class)
        else:
            admin.site.unregister(model)
            admin.site.register(model,admin_class)
    except Exception as e:
        print(f'Error registering {model.__name__}: {e}')