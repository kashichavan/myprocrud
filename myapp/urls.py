from django.urls import path
from .views import *
app_name='myapp'



urlpatterns = [
    path('viewdata/',show_view,name='show_view'),
    path('registerdata/',create_data,name='register_data'),
    path('updatedata/<int:id>',update_data,name='update_data')
]
