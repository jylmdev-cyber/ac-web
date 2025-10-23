"""
Formularios para el CMS de AC Technology
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    User, SiteConfig, HeroSection, Service, Partner,
    Showroom, Project, ContactInfo, SEOConfig
)


# ========== FORMULARIOS DE USUARIO ==========
class CustomUserCreationForm(UserCreationForm):
    """Formulario para crear usuarios con roles"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):
    """Formulario para editar usuarios"""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'phone', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ========== FORMULARIOS DEL SITIO ==========
class SiteConfigForm(forms.ModelForm):
    """Formulario para configuracion del sitio"""
    class Meta:
        model = SiteConfig
        fields = '__all__'
        widgets = {
            'site_title': forms.TextInput(attrs={'class': 'form-control'}),
            'brand_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'primary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'accent_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        }


class HeroSectionForm(forms.ModelForm):
    """Formulario para la secci�n Hero"""
    class Meta:
        model = HeroSection
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'cta1_label': forms.TextInput(attrs={'class': 'form-control'}),
            'cta1_link': forms.URLInput(attrs={'class': 'form-control'}),
            'cta1_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'cta2_label': forms.TextInput(attrs={'class': 'form-control'}),
            'cta2_link': forms.URLInput(attrs={'class': 'form-control'}),
            'cta2_icon': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    """Formulario para servicios"""
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fa-solid fa-network-wired'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'point1': forms.TextInput(attrs={'class': 'form-control'}),
            'point2': forms.TextInput(attrs={'class': 'form-control'}),
            'point3': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PartnerForm(forms.ModelForm):
    """Formulario para marcas aliadas"""
    class Meta:
        model = Partner
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ShowroomForm(forms.ModelForm):
    """Formulario para Showroom"""
    class Meta:
        model = Showroom
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    """Formulario para proyectos"""
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ContactInfoForm(forms.ModelForm):
    """Formulario para informaci�n de contacto"""
    class Meta:
        model = ContactInfo
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SEOConfigForm(forms.ModelForm):
    """Formulario para configuracion SEO"""
    class Meta:
        model = SEOConfig
        exclude = ['updated_at', 'updated_by']
        widgets = {
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '60'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'maxlength': '160'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keyword1, keyword2, keyword3'}),
            'canonical_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://actechnology.com.pe'}),
            'robots': forms.Select(attrs={'class': 'form-control'}),
            'og_title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '95'}),
            'og_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'maxlength': '200'}),
            'og_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'og_type': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_card': forms.Select(attrs={'class': 'form-control'}),
            'twitter_site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@actechnology'}),
            'twitter_creator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@usuario'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'apple_touch_icon': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'google_analytics_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'G-XXXXXXXXXX'}),
            'google_site_verification': forms.TextInput(attrs={'class': 'form-control'}),
            'bing_site_verification': forms.TextInput(attrs={'class': 'form-control'}),
            'schema_organization_name': forms.TextInput(attrs={'class': 'form-control'}),
            'schema_organization_logo': forms.URLInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
