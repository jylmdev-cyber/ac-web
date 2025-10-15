# 🌐 AC Suite — Landing + Panel de Control (Vanilla + Tailwind)

Proyecto unificado que combina la **landing page de AC Technology** y su **panel administrativo**, permitiendo editar cada sección del sitio web de forma visual sin backend, con persistencia en `localStorage`.

---

## 🚀 Características principales

- **Arquitectura 100% Vanilla JS** (sin frameworks ni build necesario).
- **Tailwind CSS CDN** con soporte de **modo oscuro** (`darkMode: 'class'`).
- **Sistema de configuración persistente (CMS local)** guardado en `localStorage`.
- **Panel administrativo** con edición visual de:
  - Hero (título, subtítulo, CTAs, imagen)
  - Servicios (título, descripción, íconos, puntos)
  - Marcas / Partners
  - Showroom (texto, imagen, enlace)
  - Proyectos
  - Contacto (email, teléfono, WhatsApp)
  - Redes sociales
  - Tema (colores primario/acento, modo claro/oscuro/sistema)
- **Sin dependencia de servidor** (totalmente estático).
- **Sincronización en tiempo real** entre `index.html` y `admin.html` usando eventos `storage`.

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
