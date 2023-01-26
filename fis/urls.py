from django.contrib import admin
from django.urls import path, include, re_path
from main.views import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/taglist/', TagAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),

    path('api/v1/create-event/', EventAPIGet.as_view({'post': 'create'})),
    path('api/v1/event/<int:pk>/', EventAPIGet.as_view({'get': 'retrieve'})),
    path('api/v1/update-event/<int:pk>/', EventAPIGet.as_view({'patch': 'update'})),
    path('api/v1/delete-event/<int:pk>/', EventAPIGet.as_view({'delete': 'destroy'})),
    path('api/v1/allevent/', EventAPIAllEvents.as_view())
]
