from django.contrib import admin

from .models import Course, Category

admin.site.site_header = "ADMIN"
admin.site.site_title = "My Mops"
admin.site.index_title = "___ADMIN___"

class CourseAdmin(admin.ModelAdmin):
    list_display= ("title", "price", "category")

class CourseInLine(admin.TabularInline):
    model = Course
    extra = 1
    exclude = ['created_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {"fields": ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
            })
    ]
    inlines = [CourseInLine]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
# Register your models here.
