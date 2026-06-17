from rest_framework import serializers
from .models import ConstructionCompany,Building





# class ConstructionCompanySerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=200)
#
# class BuildingSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=200)
#     address=serializers.CharField()
#     company_id=serializers.IntegerField()


class ConstructionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionCompany
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Building
            fields = '__all__'
            depth = 1
            # read_only_fields=['address']







