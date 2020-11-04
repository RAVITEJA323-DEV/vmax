from django.urls import path
from .views import *

urlpatterns = [

path('comment',post_detailview,name='comment'),
path('',home,name='home'),
path('mixin',post_max.as_view(),name='max'),
path('post',post_view,name='post'),
path('display',display,name='display'),
path('details',detailsapi.as_view(),name='details'),

]