from django.contrib import admin

from .models import TimeSlot, Clinic

# , BasicUser, ClinicRepresentative


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ("clinic", "reserver", "start_time", "end_time")
    list_filter = ("clinic",)
    search_fields = ("clinic__name",)


class ClinicAdmin(admin.ModelAdmin):
    list_display = ("rep", "address")
    search_fields = ("name", "address", "rep__username")
    list_filter = ("address", "name", "rep")


# class BasicUserAdmin(admin.ModelAdmin):
#     model = BasicUser


# class ClinicRepresentativeAdmin(admin.ModelAdmin):
#     model = ClinicRepresentative


admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Clinic, ClinicAdmin)
# admin.site.register(ClinicRepresentative, ClinicRepresentativeAdmin)
# admin.site.register(BasicUser, BasicUserAdmin)

