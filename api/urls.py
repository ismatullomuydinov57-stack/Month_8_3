from django.urls import path
from .views import ConstructionCompanyApiView, BuildingApiView

urlpatterns=[
path('companies/', ConstructionCompanyApiView.as_view()),
path('companies/<int:pk>/', ConstructionCompanyApiView.as_view()),
path('building/', BuildingApiView.as_view()),
path('building/<int:pk>/', BuildingApiView.as_view()),
]