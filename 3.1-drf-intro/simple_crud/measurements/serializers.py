from rest_framework import serializers
from measurements.models import Project, Measurement


class ProjectSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = '__all__'