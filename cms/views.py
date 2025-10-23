"""
Vistas para AC Technology CMS
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import (
    User, SiteConfig, HeroSection, Service, Partner,
    Showroom, Project, ContactInfo, SEOConfig
)
from .forms import (
    CustomUserCreationForm, SiteConfigForm, HeroSectionForm,
    ServiceForm, PartnerForm, ShowroomForm, ProjectForm, ContactInfoForm,
    SEOConfigForm
)


# ========== MIXINS Y DECORADORES ==========
def admin_required(user):
    """Verifica si el usuario es administrador"""
    return user.is_authenticated and (user.is_staff or user.role == 'admin')


class AdminRequiredMixin(UserPassesTestMixin):
    """Mixin para vistas que requieren ser administrador"""
    def test_func(self):
        return self.request.user.is_authenticated and \
               (self.request.user.is_staff or self.request.user.role == 'admin')


# ========== VISTA PRINCIPAL (PÚBLICA) ==========
def index(request):
    """Vista principal del sitio web (sin login requerido)"""
    context = {
        'site_config': SiteConfig.load(),
        'hero': HeroSection.load(),
        'services': Service.objects.filter(active=True),
        'partners': Partner.objects.filter(active=True),
        'showroom': Showroom.load(),
        'projects': Project.objects.filter(active=True)[:3],  # Mostrar solo 3
        'contact': ContactInfo.load(),
        'seo': SEOConfig.load(),  # Agregar configuración SEO
    }
    return render(request, 'cms/index.html', context)


# ========== DASHBOARD (REQUIERE LOGIN) ==========
@login_required(login_url='login')
def dashboard(request):
    """Dashboard principal del panel administrativo"""
    context = {
        'total_services': Service.objects.count(),
        'total_partners': Partner.objects.count(),
        'total_projects': Project.objects.count(),
        'total_users': User.objects.count(),
        'recent_projects': Project.objects.all()[:5],
        'recent_services': Service.objects.all()[:5],
    }
    return render(request, 'cms/dashboard/dashboard.html', context)


# ========== GESTIÓN DE USUARIOS (SOLO ADMIN) ==========
@user_passes_test(admin_required, login_url='dashboard')
def user_list(request):
    """Lista de usuarios"""
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'cms/dashboard/users/list.html', {'users': users})


@user_passes_test(admin_required, login_url='dashboard')
def user_create(request):
    """Crear nuevo usuario"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuario {user.username} creado exitosamente.')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'cms/dashboard/users/form.html', {
        'form': form,
        'title': 'Crear Usuario',
        'action': 'create'
    })


@user_passes_test(admin_required, login_url='dashboard')
def user_edit(request, pk):
    """Editar usuario"""
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        # Usar formulario sin password
        form = CustomUserCreationForm(request.POST, instance=user)
        form.fields.pop('password1', None)
        form.fields.pop('password2', None)

        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario {user.username} actualizado.')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
        form.fields.pop('password1', None)
        form.fields.pop('password2', None)

    return render(request, 'cms/dashboard/users/form.html', {
        'form': form,
        'title': 'Editar Usuario',
        'action': 'edit',
        'user': user
    })


@user_passes_test(admin_required, login_url='dashboard')
def user_delete(request, pk):
    """Eliminar usuario"""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'Usuario {username} eliminado.')
        return redirect('user_list')

    return render(request, 'cms/dashboard/users/delete.html', {'user': user})


# ========== CONFIGURACIÓN DEL SITIO ==========
@login_required(login_url='login')
def site_config_edit(request):
    """Editar configuración del sitio"""
    config = SiteConfig.load()

    if request.method == 'POST':
        form = SiteConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuración actualizada.')
            return redirect('dashboard')
    else:
        form = SiteConfigForm(instance=config)

    return render(request, 'cms/dashboard/config/form.html', {
        'form': form,
        'title': 'Configuración del Sitio'
    })


# ========== HERO SECTION ==========
@login_required(login_url='login')
def hero_edit(request):
    """Editar sección Hero"""
    hero = HeroSection.load()

    if request.method == 'POST':
        form = HeroSectionForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sección Hero actualizada.')
            return redirect('dashboard')
    else:
        form = HeroSectionForm(instance=hero)

    return render(request, 'cms/dashboard/hero/form.html', {
        'form': form,
        'title': 'Editar Hero'
    })


# ========== SERVICIOS ==========
class ServiceListView(LoginRequiredMixin, ListView):
    """Lista de servicios"""
    model = Service
    template_name = 'cms/dashboard/services/list.html'
    context_object_name = 'services'
    login_url = 'login'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    """Crear servicio"""
    model = Service
    form_class = ServiceForm
    template_name = 'cms/dashboard/services/form.html'
    success_url = reverse_lazy('service_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Servicio creado exitosamente.')
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    """Editar servicio"""
    model = Service
    form_class = ServiceForm
    template_name = 'cms/dashboard/services/form.html'
    success_url = reverse_lazy('service_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Servicio actualizado.')
        return super().form_valid(form)


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    """Eliminar servicio"""
    model = Service
    template_name = 'cms/dashboard/services/delete.html'
    success_url = reverse_lazy('service_list')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Servicio eliminado.')
        return super().delete(request, *args, **kwargs)


# ========== MARCAS/PARTNERS ==========
class PartnerListView(LoginRequiredMixin, ListView):
    """Lista de marcas"""
    model = Partner
    template_name = 'cms/dashboard/partners/list.html'
    context_object_name = 'partners'
    login_url = 'login'


class PartnerCreateView(LoginRequiredMixin, CreateView):
    """Crear marca"""
    model = Partner
    form_class = PartnerForm
    template_name = 'cms/dashboard/partners/form.html'
    success_url = reverse_lazy('partner_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Marca creada exitosamente.')
        return super().form_valid(form)


class PartnerUpdateView(LoginRequiredMixin, UpdateView):
    """Editar marca"""
    model = Partner
    form_class = PartnerForm
    template_name = 'cms/dashboard/partners/form.html'
    success_url = reverse_lazy('partner_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Marca actualizada.')
        return super().form_valid(form)


class PartnerDeleteView(LoginRequiredMixin, DeleteView):
    """Eliminar marca"""
    model = Partner
    template_name = 'cms/dashboard/partners/delete.html'
    success_url = reverse_lazy('partner_list')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Marca eliminada.')
        return super().delete(request, *args, **kwargs)


# ========== PROYECTOS ==========
class ProjectListView(LoginRequiredMixin, ListView):
    """Lista de proyectos"""
    model = Project
    template_name = 'cms/dashboard/projects/list.html'
    context_object_name = 'projects'
    login_url = 'login'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Crear proyecto"""
    model = Project
    form_class = ProjectForm
    template_name = 'cms/dashboard/projects/form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Proyecto creado exitosamente.')
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Editar proyecto"""
    model = Project
    form_class = ProjectForm
    template_name = 'cms/dashboard/projects/form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, 'Proyecto actualizado.')
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Eliminar proyecto"""
    model = Project
    template_name = 'cms/dashboard/projects/delete.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Proyecto eliminado.')
        return super().delete(request, *args, **kwargs)


# ========== SHOWROOM ==========
@login_required(login_url='login')
def showroom_edit(request):
    """Editar sección Showroom"""
    showroom = Showroom.load()

    if request.method == 'POST':
        form = ShowroomForm(request.POST, request.FILES, instance=showroom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Showroom actualizado.')
            return redirect('dashboard')
    else:
        form = ShowroomForm(instance=showroom)

    return render(request, 'cms/dashboard/showroom/form.html', {
        'form': form,
        'title': 'Editar Showroom'
    })


# ========== CONTACTO ==========
@login_required(login_url='login')
def contact_edit(request):
    """Editar información de contacto"""
    contact = ContactInfo.load()

    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Información de contacto actualizada.')
            return redirect('dashboard')
    else:
        form = ContactInfoForm(instance=contact)

    return render(request, 'cms/dashboard/contact/form.html', {
        'form': form,
        'title': 'Editar Contacto'
    })


# ========== SEO ==========
@login_required(login_url='login')
def seo_edit(request):
    """Editar configuración SEO"""
    seo = SEOConfig.load()

    if request.method == 'POST':
        form = SEOConfigForm(request.POST, request.FILES, instance=seo)
        if form.is_valid():
            seo_obj = form.save(commit=False)
            seo_obj.updated_by = request.user
            seo_obj.save()
            messages.success(request, 'Configuración SEO actualizada exitosamente.')
            return redirect('dashboard')
    else:
        form = SEOConfigForm(instance=seo)

    return render(request, 'cms/dashboard/seo/form.html', {
        'form': form,
        'title': 'Configuración SEO',
        'seo': seo
    })
