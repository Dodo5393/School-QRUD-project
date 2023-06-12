from django.contrib import admin
from .models import Animal,Exhibit,Visitor,Employee,FeedingSchedule,Food,Positions,AnimalHabitat,Ticket
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.



class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'date_added', 'price','edit_link')
    search_fields = ('name', 'species')
    list_filter = ('species',)
    
    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_animal_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)

    edit_link.short_description = 'edit'


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'description','edit_link')
    search_fields = ('name', 'producer')
    list_filter = ('producer',)
    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_food_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)
    edit_link.short_description = 'edit'

class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary','edit_link')
    search_fields = ('name',)
    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_positions_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)
    edit_link.short_description = 'edit'

class AnimalHabitatAdmin(admin.ModelAdmin):
    list_display = ('name','edit_link')
    search_fields = ('name',)
    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_animalhabitat_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)
    edit_link.short_description = 'edit'


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'entry_date', 'exit_date','edit_link')
    search_fields = ('name',)

    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_ticket_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)
    
    edit_link.short_description = 'edit'

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'ticket_type', 'edit_link')
    search_fields = ('name',)
    list_filter = ('ticket_type',)

    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_visitor_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)

    edit_link.short_description = 'edit'


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'start', 'end','edit_link')
    search_fields = ('name',)
    list_filter = ('location',)
    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_exhibit_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)

    edit_link.short_description = 'edit'


class FeedingScheduleAdmin(admin.ModelAdmin):
    list_display = ('animal', 'time', 'food', 'quantity','edit_link')
    search_fields = ('animal__name',)

    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_feedingschedule_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)

    edit_link.short_description = 'edit'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'edit_link')
    list_display_links = ('name',)  
    search_fields = ('name',)
    list_filter = ('position', 'salary')

    def edit_link(self, obj):
        edit_url = reverse('admin:zoo_app_employee_change', args=[obj.pk])
        return format_html('<a href="{}" class="changelink">Edit</a>', edit_url)

    edit_link.short_description = 'edit'  




admin.site.register(Animal, AnimalAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Positions, PositionsAdmin)
admin.site.register(AnimalHabitat, AnimalHabitatAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(FeedingSchedule, FeedingScheduleAdmin)
admin.site.register(Employee, EmployeeAdmin)
