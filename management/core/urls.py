from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include, url

from routines.views import ExerciseViewSet, RoutineViewSet


router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'routines', RoutineViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
