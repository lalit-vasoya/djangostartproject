from django.urls import path
from .views import SearchBookView,BookCleanerView,BooklistListView,BookorderListView,CleanerConfirm

app_name='booking'

urlpatterns = [
    path('searchbook/',SearchBookView.as_view(),name='searchbook'),
    path('bookcleaner/<int:pk>',BookCleanerView.as_view(),name='bookcleaner'),
    path('cleanerconfirm/<int:pk>',CleanerConfirm.as_view(),name='cleanerconfirm'),
    path('booklist/',BooklistListView.as_view(),name="booklist"),
    path('bookorder/',BookorderListView.as_view(),name="bookorder"),
]
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
