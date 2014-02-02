from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from core.resources import *
from tastypie.api import Api

# API REST URL Configurations
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())
v1_api.register(ListResource())
v1_api.register(SavedQueryResource())

urlpatterns = patterns('',                    
     url(r'^grappelli/', include('grappelli.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^', include(v1_api.urls)),     
)
urlpatterns += staticfiles_urlpatterns()
