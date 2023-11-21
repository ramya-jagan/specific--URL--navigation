from django.urls import path
from app2.views import *
app_name='connect1'

urlpatterns=[
  path('html2/',html2,name='html2'),
]