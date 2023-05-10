from django.urls import path, include
from .views import ZodioscopeHomeView, DailyZodioscopeView

urlpatterns = [
    path('', ZodioscopeHomeView.as_view(), name='zodioscope_home'),
    path('daily/', DailyZodioscopeView.as_view(), name='zodioscope_daily'),
]