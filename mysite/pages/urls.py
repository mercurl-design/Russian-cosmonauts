from django.contrib import admin
from django.urls import path
from pages.views import (home, titor, soloviev, padalka, krikalev, 
                        kondakova, cosmonaut_detail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cosmonaut/<int:pk>/', cosmonaut_detail, name='cosmonaut_detail'),
    path('titor/', titor, name='titor'),
    path('krikalev/', krikalev, name='krikalev'),
    path('padalka/', padalka, name='padalka'),
    path('soloviev/', soloviev, name='soloviev'),
    path('kondakova/', kondakova, name='kondakova'),
]