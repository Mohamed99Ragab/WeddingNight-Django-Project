from django.urls import path
from .views import home_page , about_page , halls_page,makeup_page,session_page,single_hall_page,single_makeup_page,single_session_page,contact_page

urlpatterns = [
    path('',home_page,name='home'),
    path('about/',about_page,name='about'),
    path('contact/',contact_page,name='contact'),
    path('halls/',halls_page,name='halls'),
    path('makeup/',makeup_page,name='makeup'),
    path('session/',session_page,name='session'),
    path('single-hall/<int:id>',single_hall_page,name='single-hall'),
    path('single-makeup/<int:id>',single_makeup_page,name='single-makeup'),
    path('single-session/<int:id>',single_session_page,name='single-session'),
    



]

app_name = 'links'