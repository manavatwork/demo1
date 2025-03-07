from django.contrib import admin
from .models import Board
# from .models import Topic,Post

# Register your models here.

# class ChaiReviewInLine(admin.TabularInline):
    # model = ChaiReview
    # extra 2

# class chaiVeraityAdmin(admin.ModelAdmin):
    # list_display = ('name','type','date_added')
    # inlines = [ChaiReviewInline]

# class StoreAdmin(admin.ModelAdmin):
#     list_display=['name','location']
    # filter_horizontal = (chai_varities)

# class ChaiCertificateAdmin(admin.ModelAdmin):
    # list_display = ('chai', 'certificates')



admin.site.register(Board)
# admin.site.register(ChaiVeraity, ChaiCertificateAdmin)
# admin.site.register()
# admin.site.register()