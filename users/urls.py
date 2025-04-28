from django.urls import path
from . import views

urlpatterns = [
    path('waitlist/', views.waitlist, name='waitlist'),
    path('waitlist/<int:id>/', views.list_detail, name='waitlist-detail'),
    path('waitlist-list/', views.WaitlistListAPIView.as_view(), name='waitlist-list-api'),
]
