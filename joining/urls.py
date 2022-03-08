from joining.views import JoinUs
#Import Libary

urlpatterns = [
    path('Join|UnitCafe', JoinUs, name='joinus'),
#    path('', include("joining.urls")),
]
