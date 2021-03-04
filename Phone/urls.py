"""Phone_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from . import views

app_name = 'Phone'
urlpatterns = [
    # path('', views.Home.as_view(), name='index'),
    # path('add', views.Add.as_view(),name='add'),
    # path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('admin/', admin.site.urls),

    #path('', views.Trademark_List.as_view(), name='phone_list'),
    path('', views.PhoneList.as_view(), name='phone_list'),
    path('view/<int:pk>', views.PhoneView.as_view(), name='phone_view'),
    path('new', views.PhoneCreate.as_view(), name='phone_new'),
    path('edit/<int:pk>', views.PhoneUpdate.as_view(), name='phone_edit'),
    path('delete/<int:pk>', views.PhoneDelete.as_view(), name='phone_delete'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('trademark', views.TrademarkResultView.as_view(), name='trademark_results'),



    # path('iphone', views.IPhoneResultsView.as_view(), name='iphone_results'),
    # path('samsung', views.SamsungResultsView.as_view(), name='samsung_results'),
    # path('nokia', views.NokiaResultsView.as_view(), name='nokia_results'),
    # path('oppo', views.OppoResultsView.as_view(), name='oppo_results'),
    # path('vsmart', views.VSmartResultsView.as_view(), name='vsmart_results'),

]
