from .models import TimeSlot, Clinic, ClinicRepresentative, BasicUser
from rest_framework import serializers


class ClinicRepresentativeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    clinics = "ClinicSerializer"

    class Meta:
        model = ClinicRepresentative
        fields = ("url", "id", "user", "clinics")


class BasicUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    reserved_slots = "TimeSlotSerializer"

    class Meta:
        model = BasicUser
        fields = ("url", "id", "user", "reserved_slots")


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    rep = ClinicRepresentativeSerializer()
    time_slots = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TimeSlot.objects.all()
    )

    class Meta:
        model = Clinic
        fields = ("name", "url", "id", "rep", "address", "time_slots")


class TimeSlotSerializer(serializers.HyperlinkedModelSerializer):
    clinic = ClinicSerializer()
    reserver = BasicUserSerializer()

    class Meta:
        model = TimeSlot
        fields = ("url", "id", "clinic", "reserver")

