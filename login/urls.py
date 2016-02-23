from django.conf.urls import url
from . import views
 
urlpatterns = [

    url(r'^$', 'django.contrib.auth.views.login'),

    url(r'^logout/$', views.logout_page),

    # If user is not login it will redirect to login page

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), 

    url(r'^register/$', views.register),

    url(r'^register/success/$', views.register_success),

    url(r'^home/$', views.home),

]
