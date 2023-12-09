"""
URL configuration for main_apka project.

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
from django.contrib import admin
from django.urls import path
from Core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('go_back_action', core_views.go_back_action, name='go_back_action'),
    path('call_page', core_views.call_page, name='call_page'),
    path('menu_page', core_views.menu_page, name='menu_page'),
    path('newsletter_page', core_views.newsletter_page, name='newsletter_page'),

    #kelner
    path('kelner_index', core_views.kelner_index, name='kelner_index'),
    path('kelner_login', core_views.kelner_login, name='kelner_login'),
    path('kelner_menu', core_views.kelner_menu, name='kelner_menu'),
    path('kelner_add_order', core_views.kelner_add_order, name='kelner_add_order'),
    path('kelner_map', core_views.kelner_map, name='kelner_map'),
    path('kelner_receipt', core_views.kelner_receipt, name='kelner_receipt'),
    path('kelner_go_back_action', core_views.kelner_go_back_action, name='kelner_go_back_action'),

]
