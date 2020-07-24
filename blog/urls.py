from django.urls import path
from . import views


urlpatterns =[
    path('', views.Home, name='home'),
    path('active/', views.ApplicationListView.as_view(), name='active-list'),
    path('applicationhistory/', views.ApplicationHistoryListView.as_view(), name='application-history'),
    path('application/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('permission/<int:pk>/reject/', views.Reject, name='permission-reject'),
    path('permission/<int:pk>/accept/', views.Accept, name='permission-accept'),
    path('pending/', views.PermissionListView.as_view(), name='pending-list'),
    path('permissionhistory/', views.PermissionHistoryListView.as_view(), name='permission-history'),
    path('permission/<int:pk>/', views.PermissionDetailView.as_view(), name='permission-detail'),
    path('application/new/', views.ApplicationCreateView.as_view(), name='application-create'),
]
