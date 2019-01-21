from django.urls import path
from core.views import portafolioList, portafolioDetail

urlpatterns = [
    path('project/', portafolioList.as_view(), name="projectList"),
    path('project/<int:pk>/',portafolioDetail.as_view() , name="projectDetail")
]