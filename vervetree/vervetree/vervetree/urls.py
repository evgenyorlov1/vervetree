from django.conf.urls import include, url
from django.contrib import admin
from pages import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vervetree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index.as_view(), name='index')
]
