# serializers.py
from rest_framework import serializers

class StepSerializer(serializers.Serializer):
    action = serializers.CharField()

class TestSerializer(serializers.Serializer):
    title = serializers.CharField()
    steps = serializers.ListField(child=serializers.CharField())

class TestDataSerializer(serializers.Serializer):
    tests = TestSerializer(many=True)
