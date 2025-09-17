from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet
from . import views
from .views import ContactMessageCreateView

router = DefaultRouter()
router.register('portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('', include(router.urls)),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact"),
]
