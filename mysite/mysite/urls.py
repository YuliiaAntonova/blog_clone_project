

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include # new

# from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]
