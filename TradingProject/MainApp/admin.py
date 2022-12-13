from django.contrib import admin
from MainApp.models import Csv
# Register your models here.

# class viewModel(admin.ModelAdmin):
#     list_display=['name','time','date',]


admin.site.register(Csv)