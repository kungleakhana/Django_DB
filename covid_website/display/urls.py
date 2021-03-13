from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('hospitail/',views.hospital,name='hospital_detail'),
    path('survey/',views.survey,name='survey'),
]