"""
URL configuration for parakeet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(
        route='pages/',
        view=include(
            arg='pages.urls',
            namespace='pages'
        )
    ),
    path(
        route='posts/',
        view=include(
            arg='posts.urls',
            namespace='posts'
        )
    ),
    path(
        route='profiles',
        view=include(
            arg='profiles.urls',
            namespace='profiles'
        )
    )
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
