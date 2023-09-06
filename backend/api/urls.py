from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'tags', views.TagViewSet)
router_v1.register(r'ingredients', views.IngredientViewSet)
router_v1.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path('users/subscriptions/',
         views.UserSubscriptionsViewSet.as_view({'get': 'list'})),
    path('users/<int:user_id>/subscribe/', views.UserSubscribeView.as_view()),
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
]
