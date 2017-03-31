"""mypnk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

admin.site.site_header = "Pur'N'Kleen"
admin.site.site_title = "PNK Administation"
admin.site.index_title = "PNK"

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^giveaway/$', views.giveaway, name='giveaway'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.ProfileDetailView.as_view(), name='my_profile'),

    #########################
    # Start About Views     #
    #########################
    url(r'^about/$', views.about, name='about'),
    url(r'^vision/$', views.vision, name='vision'),
    url(r'^values/$', views.values, name='values'),
    url(r'^team/$', views.team, name='team'),
    url(r'^benefits/$', views.benefits, name='benefits'),
    url(r'^bylaws/$', views.bylaws, name='bylaws'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^join-pnk/$', views.join_pnk, name='join-pnk'),
    #########################
    # End About Views       #
    #########################

    #########################
    # Start Solutions Views #
    #########################
    url(r'^mission-planner/$', views.mission_planner, name='mission-planner'),
    url(r'^fleet-view/$', views.fleet_view, name='fleet-view'),
    #########################
    # End Solutions Views   #
    #########################

    #########################
    # Start Services Views  #
    #########################
    url(r'^fuel-services/$', views.fuel_services, name='fuel-services'),
    url(r'^maintenance-and-repair/$', views.maintenance_repair, name='maintenance-and-repair'),
    url(r'^transportation/$', views.transportation, name='transportation'),
    url(r'^implementation/$', views.implementation, name='implementation'),
    url(r'^support-and-training/$', views.support_training, name='support-and-training'),
    url(r'^consulting-services/$', views.consulting_services, name='consulting-services'),
    url(r'^professional-services/$', views.professional_services, name='professional-services'),
    #########################
    # End Services Views    #
    #########################

    #########################
    # Start Knowledge Views #
    #########################
    url(r'^pnk-podcast/$', views.pnk_podcast, name='pnk-podcast'),
    url(r'^links-and-tools/$', views.links_tools, name='links-and-tools'),
    #########################
    # End Knowledge Views   #
    #########################
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

