from joining.views import JoinUs
from django.urls import path, include
#Import Libary

urlpatterns = [
    path('Join|UnitCafe', JoinUs, name='joinus'),
#    path('', include("joining.urls")),
]
