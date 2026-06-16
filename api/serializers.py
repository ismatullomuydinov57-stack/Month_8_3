from rest_framework import serializers

class ConstructionCompanySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=200)

class BuildingSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=200)
    address=serializers.CharField()
    company_id=serializers.IntegerField()

