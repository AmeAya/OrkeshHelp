from django.urls import path
from .views import HotWaterListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HotWaterListView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
