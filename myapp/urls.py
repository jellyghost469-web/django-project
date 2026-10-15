
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
     path('home/', views.home='home'),
      path('contact/', views.contact,name='contact'),
       path('about/', views.about,name='about'),
        path('payment/', views.payment name='payment'),
]



