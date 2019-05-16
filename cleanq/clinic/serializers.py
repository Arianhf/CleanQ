from .models import TimeSlot, Clinic, ClinicRepresentative, BasicUser
from rest_framework import serializers


class ClinicRepresentativeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = ClinicRepresentative
        fields = ("url", "id", "user")


class BasicUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = BasicUser
        fields = ("url", "id", "user")


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    rep = serializers.HyperlinkedRelatedField(view_name="representative-detail")
    time_slots = serializers.PrimaryKeyRelatedField(
        many=True, view_name="timeslot-detail", read_only=True
    )

    class Meta:
        model = Clinic
        fields = ("url", "id", "rep", "address", "time_slots")


class TimeSlotSerializer(serializers.HyperlinkedModelSerializer):
    clinic = serializers.HyperlinkedRelatedField(view_name="clinic-detail")
    reserver = serializers.HyperlinkedRelatedField(view_name="reserver-detail")

    class Meta:
        model = TimeSlot
        fields = ("url", "id", "clinic")

