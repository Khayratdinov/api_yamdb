from django.urls import include, path
from rest_framework import routers

app_name = 'api'

router_v1 = routers.DefaultRouter()

urlpatterns = [

    path('v1/', include(router_v1.urls)),
    path('v1/', include('apps.users.urls', namespace='users')),
    
]