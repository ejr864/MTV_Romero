from django.contrib import admin
from django.urls import path
from MTV_App.views import familiar
from MTV_App.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('familiar/', familiar),
    #path("familiar/", name="familiar"),

]
