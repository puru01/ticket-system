"""tickettsys URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from tickets import views
from django.conf.urls.static import static

from rest_framework import routers
from django.urls import path

urlpatterns = [
    #url(r'^', views.homepage),
    url(r'^', include('tickets.urls')),
    url(r'^', include('tickets.urls')),
    #url(r'^ticketapi$', views.Get_tickets_List.as_view()),
    url(r'^admin/', admin.site.urls),
	#url(r'', include(router.urls)),
    #path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
# Routers for automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'api/tickets', TicketViewSet)


'''