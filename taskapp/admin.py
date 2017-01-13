from django.contrib import admin

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = Task._meta.get_all_field_names()

admin.site.register(Task, TaskAdmin)