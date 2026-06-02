from django.urls import path
from .views import customer_dashboard, my_complaints,map_view,admin_dashboard,complaint_form

urlpatterns = [
    path('dashboard/', customer_dashboard),
    path('my-complaints/', my_complaints),
    path('map/', map_view),
    path('admin-dashboard/', admin_dashboard),
    path('complaint/', complaint_form),
]