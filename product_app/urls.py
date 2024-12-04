
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,RegisterUserView
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'product', ProductViewSet)

# Include the router's URL patterns in the app's URL configuration
urlpatterns = [
    path('api/', include(router.urls)),  # The URL endpoint is /api/employees/
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterUserView.as_view(),name="register"),

]