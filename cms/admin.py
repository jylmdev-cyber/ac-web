"""
Configuración del Admin de Django para AC Technology
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User, SiteConfig, HeroSection, Service, Partner,
    Showroom, Project, ContactInfo
)
from .forms import CustomUserCreationForm, CustomUserChangeForm


# ========== ADMIN DE USUARIOS ==========
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin personalizado para usuarios con roles"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('role', 'phone')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('role', 'phone')}),
    )


# ========== ADMIN DE CONFIGURACIÓN ==========
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    """Admin para configuración del sitio"""
    list_display = ['site_title', 'brand_name']

    def has_add_permission(self, request):
        # Solo permitir una instancia (Singleton)
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar
        return False


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    """Admin para sección Hero"""
    list_display = ['title', 'subtitle']

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ========== ADMIN DE CONTENIDO ==========
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin para servicios"""
    list_display = ['title', 'order', 'active', 'created_at']
    list_filter = ['active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'active']
    ordering = ['order', '-created_at']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Admin para marcas aliadas"""
    list_display = ['name', 'order', 'active', 'created_at']
    list_filter = ['active', 'created_at']
    search_fields = ['name', 'website']
    list_editable = ['order', 'active']
    ordering = ['order', 'name']


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    """Admin para Showroom"""
    list_display = ['title', 'url']

    def has_add_permission(self, request):
        return not Showroom.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin para proyectos"""
    list_display = ['title', 'category', 'featured', 'order', 'active', 'created_at']
    list_filter = ['category', 'featured', 'active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['featured', 'order', 'active']
    ordering = ['-featured', 'order', '-created_at']


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Admin para información de contacto"""
    list_display = ['email', 'phone', 'whatsapp']

    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
