"""
Modelos para el CMS de AC Technology
Maneja toda la configuración del sitio web
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# ========== MODELO DE USUARIO CON ROLES ==========
class User(AbstractUser):
    """Usuario personalizado con roles"""
    ROLES = (
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Visualizador'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='editor',
        verbose_name='Rol'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono'
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# ========== CONFIGURACIÓN DEL SITIO ==========
class SiteConfig(models.Model):
    """Configuración general del sitio (Singleton)"""
    site_title = models.CharField(
        max_length=200,
        default='AC Technology — Soluciones Integrales',
        verbose_name='Título del sitio'
    )
    brand_name = models.CharField(
        max_length=100,
        default='AC Technology',
        verbose_name='Nombre de marca'
    )
    tagline = models.CharField(
        max_length=200,
        default='Soluciones integrales: corporativo, educativo y residencial',
        verbose_name='Lema'
    )

    # Colores del tema
    primary_color = models.CharField(
        max_length=7,
        default='#2a9dff',
        verbose_name='Color primario'
    )
    accent_color = models.CharField(
        max_length=7,
        default='#00c9b7',
        verbose_name='Color de acento'
    )

    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuración del sitio'

    def save(self, *args, **kwargs):
        # Asegurar que solo exista una instancia (Singleton)
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Prevenir eliminación
        pass

    @classmethod
    def load(cls):
        """Cargar o crear la configuración del sitio"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.site_title


# ========== SECCIÓN HERO ==========
class HeroSection(models.Model):
    """Sección Hero/Principal del sitio"""
    title = models.CharField(
        max_length=200,
        default='Proyectos INTEGRALES en tecnología',
        verbose_name='Título'
    )
    subtitle = models.TextField(
        default='Integramos soluciones de audio, video, redes, domótica y seguridad.',
        verbose_name='Subtítulo'
    )
    image = models.ImageField(
        upload_to='hero/',
        blank=True,
        null=True,
        verbose_name='Imagen principal'
    )

    # CTAs (Call to Action)
    cta1_label = models.CharField(
        max_length=100,
        default='Conoce el demo virtual',
        verbose_name='Etiqueta CTA 1'
    )
    cta1_link = models.URLField(
        default='#',
        verbose_name='Enlace CTA 1'
    )
    cta1_icon = models.CharField(
        max_length=50,
        default='fa-solid fa-bolt',
        verbose_name='Icono CTA 1'
    )

    cta2_label = models.CharField(
        max_length=100,
        default='Escríbenos por WhatsApp',
        verbose_name='Etiqueta CTA 2'
    )
    cta2_link = models.URLField(
        default='#',
        verbose_name='Enlace CTA 2'
    )
    cta2_icon = models.CharField(
        max_length=50,
        default='fa-brands fa-whatsapp',
        verbose_name='Icono CTA 2'
    )

    class Meta:
        verbose_name = 'Sección Hero'
        verbose_name_plural = 'Sección Hero'

    def save(self, *args, **kwargs):
        # Singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Hero Section"


# ========== SERVICIOS ==========
class Service(models.Model):
    """Servicios ofrecidos"""
    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    icon = models.CharField(
        max_length=50,
        default='fa-solid fa-network-wired',
        help_text='Clase de FontAwesome (ej: fa-solid fa-network-wired)',
        verbose_name='Icono'
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        verbose_name='Imagen'
    )

    # Puntos clave (hasta 3)
    point1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Punto clave 1'
    )
    point2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Punto clave 2'
    )
    point3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Punto clave 3'
    )

    order = models.IntegerField(
        default=0,
        verbose_name='Orden'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.title

    @property
    def points(self):
        """Retorna lista de puntos no vacíos"""
        return [p for p in [self.point1, self.point2, self.point3] if p]


# ========== MARCAS/PARTNERS ==========
class Partner(models.Model):
    """Marcas aliadas"""
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    logo = models.ImageField(
        upload_to='partners/',
        blank=True,
        null=True,
        verbose_name='Logo'
    )
    logo_url = models.URLField(
        blank=True,
        help_text='URL alternativa del logo (si no se sube archivo)',
        verbose_name='URL del logo'
    )
    website = models.URLField(
        blank=True,
        verbose_name='Sitio web'
    )

    order = models.IntegerField(
        default=0,
        verbose_name='Orden'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Marca aliada'
        verbose_name_plural = 'Marcas aliadas'

    def __str__(self):
        return self.name

    @property
    def logo_display(self):
        """Retorna el logo a mostrar (archivo o URL)"""
        if self.logo:
            return self.logo.url
        return self.logo_url or 'https://placehold.co/400x200?text=' + self.name


# ========== SHOWROOM ==========
class Showroom(models.Model):
    """Sección de Showroom"""
    title = models.CharField(
        max_length=200,
        default='Visita nuestro Showroom',
        verbose_name='Título'
    )
    description = models.TextField(
        default='Equipado con lo último en tecnología. Agenda una demostración.',
        verbose_name='Descripción'
    )
    image = models.ImageField(
        upload_to='showroom/',
        blank=True,
        null=True,
        verbose_name='Imagen'
    )
    url = models.URLField(
        default='#',
        verbose_name='Enlace'
    )

    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showroom'

    def save(self, *args, **kwargs):
        # Singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Showroom"


# ========== PROYECTOS ==========
class Project(models.Model):
    """Proyectos realizados"""
    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name='Imagen'
    )

    # Categorías
    CATEGORIES = (
        ('educativo', 'Educativo'),
        ('corporativo', 'Corporativo'),
        ('residencial', 'Residencial'),
        ('otro', 'Otro'),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default='corporativo',
        verbose_name='Categoría'
    )

    order = models.IntegerField(
        default=0,
        verbose_name='Orden'
    )
    featured = models.BooleanField(
        default=False,
        verbose_name='Destacado'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title


# ========== INFORMACIÓN DE CONTACTO ==========
class ContactInfo(models.Model):
    """Información de contacto"""
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Formato: '+999999999'. Hasta 15 dígitos."
    )

    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        default='+51015431138',
        verbose_name='Teléfono'
    )
    email = models.EmailField(
        default='informes@actechnology.com.pe',
        verbose_name='Email'
    )
    whatsapp = models.CharField(
        validators=[phone_regex],
        max_length=17,
        default='51999999999',
        help_text='Solo números, sin +',
        verbose_name='WhatsApp'
    )
    whatsapp_message = models.TextField(
        default='Hola, me gustaría más información sobre sus soluciones integrales.',
        verbose_name='Mensaje de WhatsApp'
    )

    # Redes sociales
    facebook = models.URLField(
        blank=True,
        verbose_name='Facebook'
    )
    instagram = models.URLField(
        blank=True,
        verbose_name='Instagram'
    )
    linkedin = models.URLField(
        blank=True,
        verbose_name='LinkedIn'
    )
    youtube = models.URLField(
        blank=True,
        verbose_name='YouTube'
    )

    # Dirección física
    address = models.TextField(
        blank=True,
        verbose_name='Dirección'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Ciudad'
    )

    class Meta:
        verbose_name = 'Información de contacto'
        verbose_name_plural = 'Información de contacto'

    def save(self, *args, **kwargs):
        # Singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Información de Contacto"

    @property
    def whatsapp_url(self):
        """Genera URL de WhatsApp"""
        import urllib.parse
        base = f'https://wa.me/{self.whatsapp}'
        msg = urllib.parse.quote(self.whatsapp_message)
        return f'{base}?text={msg}'


# ========== CONFIGURACIÓN SEO ==========
class SEOConfig(models.Model):
    """Configuración SEO del sitio web (Singleton)"""

    # Meta Tags Básicos
    meta_title = models.CharField(
        max_length=60,
        default='AC Technology — Soluciones Integrales en Tecnología',
        help_text='Título que aparece en Google (máx. 60 caracteres)',
        verbose_name='Meta Title'
    )
    meta_description = models.TextField(
        max_length=160,
        default='Expertos en integración de redes, audio/video, domótica y seguridad para empresas, instituciones educativas y residencias.',
        help_text='Descripción que aparece en Google (máx. 160 caracteres)',
        verbose_name='Meta Description'
    )
    meta_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text='Palabras clave separadas por comas',
        verbose_name='Meta Keywords'
    )
    canonical_url = models.URLField(
        blank=True,
        help_text='URL canónica del sitio (ej: https://actechnology.com.pe)',
        verbose_name='URL Canónica'
    )

    # Robots
    ROBOTS_CHOICES = (
        ('index, follow', 'Index, Follow (Permitir todo)'),
        ('noindex, follow', 'No Index, Follow (No indexar, seguir enlaces)'),
        ('index, nofollow', 'Index, No Follow (Indexar, no seguir enlaces)'),
        ('noindex, nofollow', 'No Index, No Follow (Bloquear todo)'),
    )
    robots = models.CharField(
        max_length=50,
        choices=ROBOTS_CHOICES,
        default='index, follow',
        verbose_name='Robots Meta Tag'
    )

    # Open Graph (Facebook, LinkedIn, etc.)
    og_title = models.CharField(
        max_length=95,
        blank=True,
        help_text='Título para redes sociales (si está vacío, usa meta_title)',
        verbose_name='OG Title'
    )
    og_description = models.TextField(
        max_length=200,
        blank=True,
        help_text='Descripción para redes sociales (si está vacío, usa meta_description)',
        verbose_name='OG Description'
    )
    og_image = models.ImageField(
        upload_to='seo/',
        blank=True,
        null=True,
        help_text='Imagen para compartir en redes sociales (1200x630px recomendado)',
        verbose_name='OG Image'
    )
    og_type = models.CharField(
        max_length=50,
        default='website',
        help_text='Tipo de contenido (website, article, etc.)',
        verbose_name='OG Type'
    )

    # Twitter Cards
    twitter_card = models.CharField(
        max_length=50,
        choices=(
            ('summary', 'Summary'),
            ('summary_large_image', 'Summary Large Image'),
            ('app', 'App'),
            ('player', 'Player'),
        ),
        default='summary_large_image',
        verbose_name='Twitter Card Type'
    )
    twitter_site = models.CharField(
        max_length=50,
        blank=True,
        help_text='@usuario de Twitter del sitio',
        verbose_name='Twitter Site'
    )
    twitter_creator = models.CharField(
        max_length=50,
        blank=True,
        help_text='@usuario de Twitter del creador',
        verbose_name='Twitter Creator'
    )

    # Favicon
    favicon = models.ImageField(
        upload_to='seo/',
        blank=True,
        null=True,
        help_text='Favicon del sitio (32x32px o 64x64px)',
        verbose_name='Favicon'
    )

    # Apple Touch Icon
    apple_touch_icon = models.ImageField(
        upload_to='seo/',
        blank=True,
        null=True,
        help_text='Icono para dispositivos Apple (180x180px)',
        verbose_name='Apple Touch Icon'
    )

    # Google Analytics
    google_analytics_id = models.CharField(
        max_length=50,
        blank=True,
        help_text='ID de Google Analytics (ej: G-XXXXXXXXXX o UA-XXXXXXXXX-X)',
        verbose_name='Google Analytics ID'
    )

    # Google Search Console
    google_site_verification = models.CharField(
        max_length=100,
        blank=True,
        help_text='Código de verificación de Google Search Console',
        verbose_name='Google Site Verification'
    )

    # Microsoft Bing
    bing_site_verification = models.CharField(
        max_length=100,
        blank=True,
        help_text='Código de verificación de Bing Webmaster Tools',
        verbose_name='Bing Site Verification'
    )

    # Schema.org JSON-LD
    schema_organization_name = models.CharField(
        max_length=100,
        default='AC Technology',
        verbose_name='Nombre de la Organización (Schema)'
    )
    schema_organization_logo = models.URLField(
        blank=True,
        help_text='URL del logo de la organización',
        verbose_name='Logo de la Organización (Schema)'
    )

    # Otros
    author = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Autor'
    )

    # Campos de auditoría
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    updated_by = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Actualizado por'
    )

    class Meta:
        verbose_name = 'Configuración SEO'
        verbose_name_plural = 'Configuración SEO'

    def save(self, *args, **kwargs):
        # Asegurar que solo exista una instancia (Singleton)
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Prevenir eliminación
        pass

    @classmethod
    def load(cls):
        """Cargar o crear la configuración SEO"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Configuración SEO"

    def get_og_title(self):
        """Retorna og_title o meta_title como fallback"""
        return self.og_title or self.meta_title

    def get_og_description(self):
        """Retorna og_description o meta_description como fallback"""
        return self.og_description or self.meta_description

    def get_og_image_url(self):
        """Retorna URL de la imagen OG o None"""
        if self.og_image:
            return self.og_image.url
        return None
