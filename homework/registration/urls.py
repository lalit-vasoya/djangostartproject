from django.urls import path
from homework import settings
from django.conf.urls.static import static
from .views import RegistrationView,LoginView,LogoutView,ProfileDetailView,CleanerCreate

app_name='registration'

urlpatterns = [
    path('',LoginView.as_view(),name='index'),
    path('registration',RegistrationView.as_view(),name='registration'),   
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name='profile'),
    path('cleanercreate/',CleanerCreate.as_view(),name='cleanercreate'),
]
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
