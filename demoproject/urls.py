"""
demoproject URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),
    path('courier/', include('courier.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name="home")

]
