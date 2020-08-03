from django.contrib import admin
from django.conf.urls import url, include
from django.urls import include, path

from api.urls import router as api_router

urlpatterns = [
    path('grid/', include('grid.urls')),
    path('admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
]