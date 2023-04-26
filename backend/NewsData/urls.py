from django.urls import path
from .views import *

urlpatterns = [
    path("newsdata/", CombinedSerializerView.as_view())
]