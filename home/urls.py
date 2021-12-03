from django.contrib import admin
from django.urls import path,include
#from django.urls.conf import include
from home import views

#django admin header customization

admin.site_header = "Developer Abhishek"
admin.site.site_title = "Welcome to Abhishek's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    
]