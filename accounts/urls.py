from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign-in/',views.login_view,name='sign-in'),
    path('sign-up/',views.customer_signup,name='sign-up'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('customer_home/',views.customer_home,name='customer_home'),
    path('worker_home/',views.worker_home,name='worker_home'),

    path('worker-signup/', views.worker_register, name='worker-signup'),
    path('workers/', views.worker_view, name='workers'),
    path('customers/', views.customer_view, name='customers'),
]