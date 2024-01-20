from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('user', core_views.user, name='user_page'),
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
    path('kelner_index', core_views.kelner_go_back_action, name='kelner_go_back_action'),
]
