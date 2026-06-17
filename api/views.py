from django.http import FileResponse
from rest_framework import status
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView, ListCreateAPIView


from .models import ConstructionCompany, Building
from .serializers import ConstructionCompanySerializer, BuildingSerializer

class ConstructionCompanyApiView(ListCreateAPIView):
    queryset = ConstructionCompany.objects.all()
    serializer_class = ConstructionCompanySerializer

class ConstructionCompanyDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = ConstructionCompany.objects.all()
    serializer_class = ConstructionCompanySerializer


class BuildingApiView(ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id", None)
        price = self.request.query_params.get("price")

        if company_id:
            queryset = Building.objects.filter(company_id=company_id)
        else:
            queryset = Building.objects.all()

        if price == "high":
            queryset = queryset.order_by("-price")
        elif price == "low":
            queryset = queryset.order_by("price")

        return queryset
    lokkup_url_kwarg='category_id'


class BuildingDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


# class ConstructionCompanyApiView(APIView):
#     def get(self,request:Request, pk:int=None):
#         if not pk:
#             companies=ConstructionCompany.objects.all()
#             return Response(ConstructionCompanySerializer(companies, many=True).data)
#         else:
#             return Response(ConstructionCompanySerializer(ConstructionCompany.objects.get(pk=pk)).data)
#
#     def post(self, request:Request, pk:int=None):
#         if not pk:
#             serializer=ConstructionCompanySerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             company=ConstructionCompany.objects.create(**serializer.validated_data)
#             return Response(ConstructionCompanySerializer(company).data)
#         else:
#             return Response({'message':'Method POST not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     def put(self, request:Request, pk:int=None):
#         if not pk:
#             return Response({'message': 'Method POST not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             company=get_object_or_404(ConstructionCompany, pk=pk)
#             serializer=ConstructionCompanySerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             company.name=serializer.validated_data.get("name", company.name)
#             company.save()
#             return Response(ConstructionCompanySerializer(company).data)
#     def delete(self, request:Request, pk:int=None):
#         company=get_object_or_404(ConstructionCompany, pk=pk)
#         company.delete()
#         return Response({'message':'Company deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#
#
# class BuildingApiView(APIView):
#     def get(self,request:Request, pk:int=None):
#         if not pk:
#             buildings=Building.objects.all()
#             return Response(BuildingSerializer(buildings, many=True).data)
#         else:
#             return Response(BuildingSerializer(Building.objects.get(pk=pk)).data)
#
#     def post(self, request:Request, pk:int=None):
#         if not pk:
#             serializer=BuildingSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             building=Building.objects.create(**serializer.validated_data)
#             return Response(BuildingSerializer(building).data)
#         else:
#             return Response({'message':'Method POST not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     def put(self, request:Request, pk:int=None):
#         if not pk:
#             return Response({'message': 'Method POST not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             building=get_object_or_404(Building, pk=pk)
#             serializer=BuildingSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             building.name=serializer.validated_data.get("name", building.name)
#             building.save()
#             return Response(BuildingSerializer(building).data)
#     def delete(self, request:Request, pk:int=None):
#         building=get_object_or_404(Building, pk=pk)
#         building.delete()
#         return Response({'message':'Building deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#
#




