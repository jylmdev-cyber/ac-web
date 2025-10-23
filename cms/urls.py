"""
URLs para la aplicación CMS
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ========== PÁGINA PRINCIPAL (PÚBLICA) ==========
    path('', views.index, name='index'),

    # ========== AUTENTICACIÓN ==========
    path('login/', auth_views.LoginView.as_view(template_name='cms/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # ========== DASHBOARD (REQUIERE LOGIN) ==========
    path('panel-admin/', views.dashboard, name='panel-admin'),
    path('panel-admin/dashboard/', views.dashboard, name='dashboard'),

    # ========== GESTIÓN DE USUARIOS (SOLO ADMIN) ==========
    path('panel-admin/users/', views.user_list, name='user_list'),
    path('panel-admin/users/create/', views.user_create, name='user_create'),
    path('panel-admin/users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('panel-admin/users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # ========== CONFIGURACIÓN ==========
    path('panel-admin/config/', views.site_config_edit, name='site_config_edit'),
    path('panel-admin/hero/', views.hero_edit, name='hero_edit'),

    # ========== SERVICIOS ==========
    path('panel-admin/services/', views.ServiceListView.as_view(), name='service_list'),
    path('panel-admin/services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('panel-admin/services/<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('panel-admin/services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # ========== MARCAS ==========
    path('panel-admin/partners/', views.PartnerListView.as_view(), name='partner_list'),
    path('panel-admin/partners/create/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('panel-admin/partners/<int:pk>/edit/', views.PartnerUpdateView.as_view(), name='partner_edit'),
    path('panel-admin/partners/<int:pk>/delete/', views.PartnerDeleteView.as_view(), name='partner_delete'),

    # ========== PROYECTOS ==========
    path('panel-admin/projects/', views.ProjectListView.as_view(), name='project_list'),
    path('panel-admin/projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('panel-admin/projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('panel-admin/projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # ========== SHOWROOM ==========
    path('panel-admin/showroom/', views.showroom_edit, name='showroom_edit'),

    # ========== CONTACTO ==========
    path('panel-admin/contact/', views.contact_edit, name='contact_edit'),

    # ========== SEO ==========
    path('panel-admin/seo/', views.seo_edit, name='seo_edit'),
]
