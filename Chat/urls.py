from django.urls import path
from .views import *

urlpatterns = [

path('comment',post_detailview,name='comment'),
path('post',post_view,name='post'),
path('mixin',post_max.as_view(),name='max'),

]