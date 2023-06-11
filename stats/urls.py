from django.urls import path
from .views import SiteList, ActionList, ActionDetail

urlpatterns = [
    path('sites/', SiteList.as_view(), name='site-list'),
    path('actions/', ActionList.as_view(), name='action-list'),
    path('actions/<int:pk>/', ActionDetail.as_view(), name='action-detail'),
]
