"""
URL configuration for djadmin_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.urls import include

### add import for django debug toolbar
from djadmin_config.settings import IS_DEVELOPMENT
from djadmin_config.settings import IS_USING_DJDT

### uncomment when using DJDT
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('', include('djapp.djapp_import_export.urls', namespace='app_import_export')),
    path('admin/', admin.site.urls),
]


if IS_DEVELOPMENT:
    if IS_USING_DJDT:
        '''
        '''
        ### uncomment when using DJDT
        urlpatterns += debug_toolbar_urls()

### change title words in django admin pages
admin.site.site_header = "Import Export Administration"
admin.site.site_title = "Import Export Admin Portal"
admin.site.index_title = "Welcome to Import Export Portal"

