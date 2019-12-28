from django.conf.urls import url,include
from basicapp import views


urlpatterns=[
  url(r'^relative/$',views.relative,name='relative'),
  url(r'^other/$',views.other,name='other'),
  url(r'^base/$',views.base,name='base'),
  url(r'^register/$',views.register,name='register'),
  url(r'^login/$',views.user_login,name='login'),
]
