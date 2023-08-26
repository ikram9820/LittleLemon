from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('booking/tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
]


urlpatterns += router.urls