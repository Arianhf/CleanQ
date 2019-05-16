from django.contrib import admin

from .models import TimeSlot, Clinic, BasicUser, ClinicRepresentative


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ("clinic", "reserver", "start_time", "end_time")


class ClinicAdmin(admin.ModelAdmin):
    list_display = ("rep", "address")


class BasicUserAdmin(admin.ModelAdmin):
    model = BasicUser


class ClinicRepresentativeAdmin(admin.ModelAdmin):
    model = ClinicRepresentative


admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(ClinicRepresentative, ClinicRepresentativeAdmin)
admin.site.register(BasicUser, BasicUserAdmin)

