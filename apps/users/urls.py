# from django.urls import include, path
# # ============================================================================ #
# from rest_framework import routers
# # ============================================================================ #
# from .views import SignupView, TokenView, UsersViewSet


# # ============================================================================ #
# app_name = 'users'

# auth_v1 = routers.DefaultRouter()
# auth_v1.register('signup', SignupView, basename='signup')



# users_v1 = routers.DefaultRouter()
# users_v1.register('', UsersViewSet, basename='users')

# urlpatterns = [

#     path('auth/token/', TokenView, name='token'),
#     path('auth/', include(auth_v1.urls)),
#     path('users/', include(users_v1.urls)),

# ]


# ============================================================================ #'



from django.urls import include, path
from rest_framework import routers

from .views import (APISendCode, APISendToken, UserViewSet)

app_name = 'api'


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('auth/signup/', APISendCode.as_view(), name='signup'),
    path('auth/token/', APISendToken.as_view(), name='get_token'),
    path('', include(router.urls)),
]