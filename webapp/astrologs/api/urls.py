from django.urls import path
from .views import ZodioscopeDailyAPIView, DetailZodioscopeDailyAPIView

urlpatterns = [
    path('zodioscope_daily/', ZodioscopeDailyAPIView.as_view(), name='zodioscope_daily_api'),
    path('zodioscope_daily/<int:pk>', DetailZodioscopeDailyAPIView.as_view(), name='detail_zodioscope_daily_api')
]