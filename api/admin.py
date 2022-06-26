from django.contrib import admin
from .models import Doctor, Direction



class DoctorInline(admin.TabularInline):
    model = Doctor.direction.through


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'directions', 'slug', 'description', 'birthday', 'work_experience')
    search_fields = ['name', 'id', 'directions', 'slug', 'description', 'birthday', 'work_experience']
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name', 'slug', 'description', 'birthday', 'work_experience')
    ordering = ('id', 'name', 'slug', 'description', 'birthday', 'work_experience')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DoctorInline]

    def directions(self, obj):
        return "\n".join([p.name for p in obj.direction.all()])


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name')
    search_fields = ['id', 'slug', 'name']
    list_display_links = ('id', 'name')
    list_filter = ('id', 'slug', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Direction, DirectionAdmin)
