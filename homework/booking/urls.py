from django.urls import path
from .views import BookingView

app_name='booking'

urlpatterns = [
    path('book/',BookingView.as_view(),name='book'),
]
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
