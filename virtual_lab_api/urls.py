"""virtual_lab_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import redirect_view, BangladeshData
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = ' '
# admin.site.site_title = 'Admin | VL'
# admin.site.index_title = 'Admin | VL'

urlpatterns = [
    path('',redirect_view),
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("users/", include('users.urls')),
    path("projects/", include('project_management.urls')),
    path("schedules/", include('schedules.urls')),
    path("tools/", include('tools.urls')),
    path("bangladesh/",BangladeshData.as_view())
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
