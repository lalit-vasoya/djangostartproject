from django.urls import path
from .views import RegistrationView,LoginView,LogoutView
from django.conf.urls.static import static
from homework import settings

urlpatterns = [
    path('registration',RegistrationView.as_view(),name="registration"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LoginView.as_view(),name="logout"),
]
# +static(settings.STATIC)
