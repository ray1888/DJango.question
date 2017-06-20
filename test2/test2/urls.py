"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from authe import views as authe_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', authe_view.index, name='index'),
    url(r'^contact/', authe_view.contact, name='contact'),
    url(r'^signup', authe_view.signup, name='signup'),
    url(r'^signin', authe_view.signin, name='signin'),
    url(r'^logout', authe_view.logout, name='logout'),
    url(r'^tiqu', authe_view.tiqu, name='tiqu'),
    url(r'^xuanran', authe_view.xuanranwj, name='xuanranwj'),
    url(r'^txcg', authe_view.jieshou, name='jieshou'),
    url(r'^editor', authe_view.editor, name='editor'),
    url(r'^teditor', authe_view.teditor, name='teditor'),
    url(r'houtai', authe_view.houtai, name='houtai'),
    url(r'cjwj', authe_view.create_houtai, name='create_houtai'),
    url(r'myques', authe_view.myques, name='myques'),
    url(r'delete', authe_view.deleteque, name='delete'),
    url(r'^genggaipw', authe_view.genggaipw, name='genggaipw'),
    url(r'^Tongji', authe_view.Tongji, name='Tongji'),
    url(r'^Guanlian', authe_view.Guanlian, name='Guanlian'),
    url(r'^GLPrint', authe_view.GLPrint, name='GLPrint'),
    url(r'^Chongzhipw', authe_view.Chongzhipw, name='Chongzhipw'),
    url(r'^Duibi', authe_view.Duibi, name='Duibi'),
    url(r'^DBPrint', authe_view.DBPrint, name='DBPrint'),
]
