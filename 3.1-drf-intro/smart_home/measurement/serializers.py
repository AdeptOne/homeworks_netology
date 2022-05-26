from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'photo']


class CreateMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'photo', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = CreateMeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']


