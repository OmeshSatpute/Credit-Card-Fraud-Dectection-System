"""
URL configuration for FDS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('LOGOUT/',userLogout,name='userLogout'),
    path('about/',about,name='about'),
    path('dashboard/',dashboard,name='dashboard'),
    path('reports/',reports,name='reports'),
    path('upload_credit_data/',upload_credit_data,name='upload_credit_data'),
    path('prediction_button/<int:id>',prediction_button,name='prediction_button'),
    
    #for main adminstrator upload 
    
    path('upload_data/',upload_data,name='upload_data'),
    path('delete_data/<int:id>/',delete_data,name='delete_data'),

    path('enter_form_data_manually/',enter_form_data_manually,name='enter_form_data_manually'),
    path('add_files_single/<int:id>',add_files_single,name='add_files_single'),
    path('add_files_multi/<int:id>',add_files_multi,name='add_files_multi'),

    path('predict_data_manually/',predict_data_manually,name='predict_data_manually'),
    path('predict_csv_single/<int:id>',predict_csv_single,name='predict_csv_single'),
    path('predict_csv_multi/<int:id>',predict_csv_multi,name='predict_csv_multi'),

    path('account_details/',account_details,name='account_details'),
    path('change_password/',change_password,name='change_password'),
    path('analysis/<int:id>/',analysis,name='analysis'),
    path('view_data/<int:id>',view_data,name='view_data'),
    path('retrieve_data_by_id/<int:id>/',retrieve_data_by_id,name='retrieve_data_by_id'),
    
    path('admin/', admin.site.urls),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
