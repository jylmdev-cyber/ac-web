# AC Technology - Sistema de Gestión de Contenidos (CMS) con Django

Proyecto Django completo que integra los archivos HTML del repositorio en un sistema CMS funcional con panel administrativo.

## 🚀 Características

✅ **Sitio web público** - Visible sin necesidad de autenticación
✅ **Panel administrativo** (`/panel-admin`) - Requiere autenticación
✅ **Gestión de imágenes** - Sube archivos en lugar de usar URLs (con fallback a placeholder)
✅ **Sistema de usuarios con roles** - Admin, Editor, Visualizador
✅ **CRUD completo** - Para todos los modelos desde el dashboard
✅ **Responsive** - Diseño adaptable con Tailwind CSS
✅ **Modelos Singleton** - Para configuraciones únicas (Hero, Showroom, Contacto, etc.)

## 📋 Requisitos

- Python 3.11+
- Django 5.2.7
- Pillow (para manejo de imágenes)

## 🔧 Instalación

### 1. Instalar dependencias

```bash
pip install django pillow
```

### 2. Crear migraciones (ya realizado)

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 3. Crear superusuario

```bash
python3 manage.py createsuperuser
```

Sigue las instrucciones e ingresa:
- Usuario (ej: `admin`)
- Email (ej: `admin@actechnology.com`)
- Contraseña

### 4. Cargar datos iniciales (opcional)

Puedes crear datos de prueba desde el panel admin o usando el shell de Django:

```bash
python3 manage.py shell
```

```python
from cms.models import SiteConfig, HeroSection, ContactInfo, Showroom

# Crear configuración inicial
SiteConfig.objects.create()
HeroSection.objects.create()
ContactInfo.objects.create()
Showroom.objects.create()
```

### 5. Ejecutar servidor de desarrollo

```bash
python3 manage.py runserver
```

## 🌐 URLs del Proyecto

### Sitio Público (Sin autenticación requerida)
- **Inicio**: `http://localhost:8000/` o `http://localhost:8000/`
  - Muestra toda la información del sitio (Hero, Servicios, Marcas, Showroom, Proyectos, Contacto)

### Panel Administrativo (Requiere autenticación)
- **Login**: `http://localhost:8000/login/`
- **Dashboard**: `http://localhost:8000/panel-admin/`
- **Cerrar sesión**: `http://localhost:8000/logout/`

### Gestión de Contenido (Requiere login)

**Servicios:**
- Lista: `/panel-admin/services/`
- Crear: `/panel-admin/services/create/`
- Editar: `/panel-admin/services/<id>/edit/`
- Eliminar: `/panel-admin/services/<id>/delete/`

**Marcas:**
- Lista: `/panel-admin/partners/`
- Crear: `/panel-admin/partners/create/`
- Editar: `/panel-admin/partners/<id>/edit/`
- Eliminar: `/panel-admin/partners/<id>/delete/`

**Proyectos:**
- Lista: `/panel-admin/projects/`
- Crear: `/panel-admin/projects/create/`
- Editar: `/panel-admin/projects/<id>/edit/`
- Eliminar: `/panel-admin/projects/<id>/delete/`

**Usuarios (Solo Admin):**
- Lista: `/panel-admin/users/`
- Crear: `/panel-admin/users/create/`
- Editar: `/panel-admin/users/<id>/edit/`
- Eliminar: `/panel-admin/users/<id>/delete/`

**Configuración:**
- Sitio: `/panel-admin/config/`
- Hero: `/panel-admin/hero/`
- Showroom: `/panel-admin/showroom/`
- Contacto: `/panel-admin/contact/`

## 📁 Estructura del Proyecto

```
ac-web/
├── acweb/                  # Proyecto Django principal
│   ├── settings.py         # Configuración del proyecto
│   ├── urls.py            # URLs principales
│   └── wsgi.py
├── cms/                    # Aplicación CMS
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas del sitio y dashboard
│   ├── forms.py           # Formularios
│   ├── admin.py           # Configuración del admin de Django
│   ├── urls.py            # URLs de la aplicación
│   └── templates/cms/     # Templates
│       ├── index.html     # Página principal
│       ├── auth/          # Login
│       └── dashboard/     # Templates del panel admin
├── assets/                # Archivos estáticos (CSS, JS)
├── media/                 # Archivos subidos por usuarios
├── html_backup/           # HTML originales del repositorio
├── manage.py             # Comando de gestión de Django
└── db.sqlite3            # Base de datos SQLite
```

## 🎨 Modelos del Sistema

### Modelos Principales

1. **User** - Usuarios con roles (Admin, Editor, Visualizador)
2. **SiteConfig** - Configuración general del sitio (Singleton)
3. **HeroSection** - Sección principal del sitio (Singleton)
4. **Service** - Servicios ofrecidos
5. **Partner** - Marcas aliadas
6. **Project** - Proyectos realizados
7. **Showroom** - Información del showroom (Singleton)
8. **ContactInfo** - Información de contacto (Singleton)

### Condicional de Imágenes

Todos los templates implementan la condicional solicitada:

```django
{% if object.image %}
  <img src="{{ object.image.url }}" alt="{{ object.title }}"/>
{% else %}
  <img src="https://placehold.co/800x600?text=Placeholder" alt="{{ object.title }}"/>
{% endif %}
```

## 👥 Sistema de Roles

### Admin
- Acceso completo a todas las funciones
- Puede crear, editar y eliminar usuarios
- Puede gestionar todo el contenido

### Editor
- Puede crear y editar contenido
- No puede gestionar usuarios
- Acceso al dashboard y todas las secciones

### Visualizador
- Solo puede ver el contenido
- No puede crear ni editar
- Acceso limitado al dashboard

## 🔐 Credenciales de Prueba

Después de crear el superusuario, puedes crear usuarios adicionales desde:
`/panel-admin/users/create/`

O usar el admin de Django:
`http://localhost:8000/admin/`

## 📝 Notas Importantes

1. **Archivos Media**: Los archivos subidos se guardan en `/media/` según el tipo:
   - `/media/hero/` - Imágenes de la sección hero
   - `/media/services/` - Imágenes de servicios
   - `/media/partners/` - Logos de marcas
   - `/media/projects/` - Imágenes de proyectos
   - `/media/showroom/` - Imagen del showroom

2. **Assets Estáticos**: Los archivos CSS/JS originales están en `/assets/`

3. **Singleton Models**: Algunos modelos solo permiten una instancia (SiteConfig, HeroSection, Showroom, ContactInfo). No puedes crear múltiples registros.

4. **Acceso Público**: El sitio principal (`/`) es público y no requiere autenticación.

5. **Dashboard Privado**: El acceso a `/panel-admin` requiere estar autenticado.

## 🚨 Solución de Problemas

### Error: No module named 'cms'
```bash
# Verifica que estás en el directorio correcto
cd /home/user/ac-web
python3 manage.py runserver
```

### Error: OperationalError at /
```bash
# Ejecuta las migraciones
python3 manage.py migrate
```

### No puedo acceder al dashboard
- Asegúrate de haber iniciado sesión en `/login/`
- Verifica que el usuario exista en la base de datos

### Las imágenes no se muestran
- Verifica que DEBUG=True en settings.py (para desarrollo)
- Asegúrate de que las URLs de media estén configuradas correctamente

## 🎯 Próximos Pasos

1. Crear un superusuario
2. Acceder al dashboard en `/panel-admin/`
3. Configurar el sitio desde `/panel-admin/config/`
4. Agregar servicios, proyectos y marcas
5. Ver el resultado en la página principal `/`

## 📚 Documentación de Django

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)
- [Django Forms](https://docs.djangoproject.com/en/5.2/topics/forms/)

## 📄 Licencia

Este proyecto está desarrollado para AC Technology.

---

**Desarrollado con Django 5.2.7 + Tailwind CSS**
