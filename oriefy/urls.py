"""oriefy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from employees.admin import employee_admin_site
from ledger.admin import ledger_admin_site

# Admin Settings
admin.site.site_header = "Oriefy Admin"
admin.site.site_title = "Oriefy Admin Portal"
admin.site.index_title = "Welcome to Oriefy Management Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/admin', employee_admin_site.urls),
    path('ledger/', ledger_admin_site.urls),
    path('sop/', include('sop.urls')),
    path('', include('oriefy_site.urls')),
]
