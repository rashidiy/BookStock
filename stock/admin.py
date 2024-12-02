from django.contrib import admin

from stock.models import Category, Book, AdditionalInfo, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
