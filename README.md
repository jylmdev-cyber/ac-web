# 🌐 AC Suite — Landing + Panel de Control

Proyecto que combina la **landing page de AC Technology** con un **sistema de gestión de contenidos (CMS)** completo.

## 🎯 Versiones Disponibles

### 1. **Versión Vanilla JS** (Archivos HTML originales)
- 100% JavaScript Vanilla (sin frameworks)
- Persistencia en `localStorage`
- Sin backend necesario
- **Ubicación**: `/html_backup/`

### 2. **Versión Django** (Integración Completa) ⭐ **NUEVA**
- Framework Django 5.2.7
- Base de datos SQLite
- Panel administrativo completo
- Gestión de usuarios con roles
- Subida de archivos/imágenes
- **Documentación**: Ver `DJANGO_README.md`

---

## 🚀 Características de la Versión Django

✅ **Sitio web público** - Accesible sin autenticación
✅ **Panel administrativo** (`/panel-admin`) - Con autenticación requerida
✅ **Gestión de imágenes** - Sube archivos o usa URLs externas
✅ **Sistema de usuarios** - Con roles: Admin, Editor, Visualizador
✅ **CRUD completo** - Para todos los modelos desde el dashboard
✅ **Templates dinámicos** - Condicionales para mostrar imágenes o placeholders
✅ **Responsive Design** - Con Tailwind CSS
✅ **Base de datos** - SQLite (desarrollo) / PostgreSQL/MySQL (producción)

### Gestión de Contenido

- **Hero Section** - Sección principal con título, subtítulo, CTAs e imagen
- **Servicios** - CRUD completo con iconos, puntos clave e imágenes
- **Marcas Aliadas** - Logos de partners con orden personalizable
- **Showroom** - Información y enlace al showroom
- **Proyectos** - Casos destacados con categorías y destacados
- **Contacto** - Información completa con redes sociales
- **Usuarios** - Gestión de usuarios con roles y permisos

---

## 🚦 Inicio Rápido - Versión Django

### Instalación

```bash
# 1. Instalar dependencias
pip install django pillow

# 2. Aplicar migraciones
python3 manage.py migrate

# 3. Crear superusuario
python3 manage.py createsuperuser

# 4. Ejecutar servidor
python3 manage.py runserver

# 5. Acceder al sitio
# Página principal: http://localhost:8000/
# Panel admin: http://localhost:8000/panel-admin/
```

Ver `DJANGO_README.md` para documentación completa.

---

## 📂 Estructura del Proyecto

A continuación se detalla la organización de los archivos y directorios del proyecto.

```
.
├── index.html        # Landing page pública
├── admin.html        # Panel de administración
│
├── assets/
│   ├── cms.js        # Modelo de datos global + persistencia
│   ├── site.js       # Render dinámico de la landing
│   ├── admin.js      # Lógica del panel (formularios, import/export, etc.)
│   └── styles.css    # Estilos globales y utilidades personalizadas
│
├── components/
│   ├── header.html   # Encabezado y menú principal
│   ├── footer.html   # Pie de página con redes sociales
│   └── panel.html    # Drawer del panel de control (componentizado)
│
└── sections/
    ├── hero.html       # Sección principal (hero/banner)
    ├── servicios.html  # Listado de servicios
    ├── marcas.html     # Logos de partners
    ├── showroom.html   # Llamado a visitar el showroom
    ├── proyectos.html  # Casos destacados
    └── contacto.html   # Formulario de contacto y datos
```
