from django.urls import path
from .views import ConstructionCompanyApiView, ConstructionCompanyDetailApiView,BuildingApiView, BuildingDetailApiView

urlpatterns=[
path('companies/', ConstructionCompanyApiView.as_view()),
path('companies/<int:pk>/', ConstructionCompanyDetailApiView.as_view()),
path('buildings/', BuildingApiView.as_view()),
path('buildings/<int:pk>/', BuildingDetailApiView.as_view()),
path('buildings/<int:company_id>/', BuildingApiView.as_view()),
]