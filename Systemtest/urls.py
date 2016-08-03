from django.conf.urls import include,url
from django.contrib import admin
from login import views as login_views
from login.views import mylogin
from django.contrib.auth import urls as auth_urls
admin.autodiscover()

urlpatterns = [
    # url(r'^$',serve_views.home,name='home'),
    # url(r'^accounts/', include(auth_urls, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$',include('login.urls')),
    url(r'^home/',login_views.home,name='home'),
    # url(r'^accounts/', include('login.urls')),
    url(r'^add/',login_views.add,name='add'),
    url(r'^show/',login_views.showCount,name='show'),
    url(r'^recover/',login_views.recover,name='recover'),
    url(r'^edit/',login_views.edit,name='edit'),
    url(r'^login/',login_views.mylogin,name='mylogin'),
    url(r'^delete/', login_views.delete, name='delete'),
    url(r'^welcome/',login_views.welcome,name='welcome')
]