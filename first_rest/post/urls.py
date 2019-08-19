
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework -> router -> url (라우터로 url 구성해야함)

router = DefaultRouter() #디펄트 라우터를 설정해주고 우리가 라우팅할 각 api리스트를 다 띄워줄 수 있다(밑에 처럼 등록하면!)
router.register('post', views.PostViewSet) #요기에 url 네이밍을 해주는거야~!


urlpatterns = [
    path('', include(router.urls)),
]