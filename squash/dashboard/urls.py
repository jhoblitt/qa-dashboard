from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

<<<<<<< HEAD
router = DefaultRouter()
router.register(r'job', views.JobViewSet)
router.register(r'metric', views.MetricViewSet)
=======
api_router = DefaultRouter()
api_router.register(r'jobs', views.JobViewSet)
api_router.register(r'metrics', views.MetricViewSet)
api_router.register(r'packages', views.PackageViewSet)
>>>>>>> b962845... Make all API resource collection endpoints plural

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^(?P<pk>[0-9]+)/dashboard/',
        views.MetricDashboardView.as_view(),
        name='metric-detail'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
