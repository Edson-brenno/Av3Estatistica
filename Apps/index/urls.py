from django.urls import path
from Apps.index.views import index

urlpatterns = [
    path('', index, name='index'),
]