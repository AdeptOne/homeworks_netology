from django.urls import path

from measurement.views import SensorView, RetrieveUpdateSensorView, CreateMeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
]
