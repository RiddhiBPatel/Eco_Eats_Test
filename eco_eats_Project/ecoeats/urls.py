
from django.conf.urls import url
from ecoeats import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^add_feedback/', views.add_feedback, name='add_feedback') 
]
