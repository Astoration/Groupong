from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^login$',views.loginPage,name='loginPage'),
	url(r'^register$',views.registerPage,name='registerPage'),
	url(r'^registers$',views.register,name="register"),
	url(r'^logins$',views.login,name="login"),
	url(r'^detail',views.detail,name="detail")
]