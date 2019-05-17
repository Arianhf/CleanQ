from .models import TimeSlot, Clinic, ClinicRepresentative, BasicUser
from rest_framework import serializers
from users.serializers import CustomUserSerializer


class TimeSlotSerializer(serializers.HyperlinkedModelSerializer):
    # clinic = serializers.ReadOnlyField(source="clinic.name")
    clinic_name = serializers.ReadOnlyField(source="clinic.name")
    clinic_url = serializers.HyperlinkedIdentityField(view_name="clinic-detail")
    reserver_url = serializers.HyperlinkedIdentityField(
        view_name="user-detail", allow_null=True
    )

    class Meta:
        model = TimeSlot
        fields = (
            "url",
            "id",
            "start_time",
            "end_time",
            "clinic_name",
            "clinic_url",
            "reserver_url",
        )


class ClinicRepresentativeSerializer(serializers.HyperlinkedModelSerializer):
    user = CustomUserSerializer(required=True)
    clinics = serializers.StringRelatedField(many=True)

    class Meta:
        model = ClinicRepresentative
        fields = ("url", "id", "user", "clinics")


class BasicUserSerializer(serializers.HyperlinkedModelSerializer):
    user = CustomUserSerializer(required=True)
    reserved_slots = TimeSlotSerializer(many=True)

    class Meta:
        model = BasicUser
        fields = ("url", "id", "user", "reserved_slots")


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    rep = ClinicRepresentativeSerializer(required=True)

    time_slots = TimeSlotSerializer(many=True, read_only=True)

    class Meta:
        model = Clinic
        fields = ("name", "url", "id", "address", "rep", "time_slots")

