"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

# ! include sirve para traer urls de las aplicaciones
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home.urls")),
    path("producto/", include("producto.urls")),
    path("faq/", include("faq.urls")),
    path("Nosotros/", include("Nosotros.urls")),
    path("productoscompra/", include("productoscompra.urls")),
    path("productosventa/", include("productosventa.urls")),
    path("work/", include("work.urls")),
    path("showplus/", include("showplus.urls")),
    path("blog01JM/", include("blog01JM.urls")),
    path("blog02EH/", include("blog02EH.urls")),
    path("blog03PC/", include("blog03PC.urls")),
    path("customerx/", include("customerx.urls")),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
