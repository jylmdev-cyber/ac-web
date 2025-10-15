import { $, $$, initialState, loadState, saveState, resetState, applyTheme, whatsAppURL } from './cms.js';

const sections = [
  { id:'s-dashboard', label:'Dashboard' },
  { id:'s-hero', label:'Hero / Inicio' },
  { id:'s-servicios', label:'Servicios' },
  { id:'s-marcas', label:'Marcas' },
  { id:'s-showroom', label:'Showroom' },
  { id:'s-proyectos', label:'Proyectos' },
  { id:'s-contacto', label:'Contacto' },
  { id:'s-links', label:'Redes & Links' },
  { id:'s-tema', label:'Tema' },
];

let state = loadState();

function build(){
  applyTheme(state);
  // title
  document.title = 'Panel Administrativo — ' + state.site.brand;
  // icons
  $('#i-theme').className = document.documentElement.classList.contains('dark') ? 'fa-solid fa-sun text-lg' : 'fa-solid fa-moon text-lg';

  const content = $('#content');
  content.innerHTML = '';

  // Dashboard (resumen + acciones)
  content.appendChild(elSection('s-dashboard', `
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 shadow-soft border border-slate-200 dark:border-slate-800">
        <p class="text-sm text-slate-500">Marca</p>
        <p class="text-xl font-semibold">${state.site.brand}</p>
      </div>
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 shadow-soft border border-slate-200 dark:border-slate-800">
        <p class="text-sm text-slate-500">Servicios</p>
        <p class="text-xl font-semibold">${state.services.length}</p>
      </div>
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 shadow-soft border border-slate-200 dark:border-slate-800">
        <p class="text-sm text-slate-500">Proyectos</p>
        <p class="text-xl font-semibold">${state.projects.length}</p>
      </div>
    </div>
    <div class="mt-6 flex gap-3 flex-wrap">
      <a href="index.html" target="_blank" class="inline-flex items-center gap-2 rounded-xl bg-primary-600 px-4 py-2 text-white hover:bg-primary-700"><i class="fa-regular fa-eye"></i> Ver Landing</a>
      <button id="btn-export" class="inline-flex items-center gap-2 rounded-xl border px-4 py-2 hover:bg-slate-50 dark:hover:bg-slate-800"><i class="fa-solid fa-download"></i> Exportar JSON</button>
      <label class="inline-flex items-center gap-2 rounded-xl border px-4 py-2 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer">
        <i class="fa-solid fa-upload"></i> Importar JSON
        <input id="file-import" type="file" accept="application/json" class="hidden">
      </label>
      <button id="btn-reset-all" class="inline-flex items-center gap-2 rounded-xl border border-red-500 text-red-600 px-4 py-2 hover:bg-red-50"><i class="fa-solid fa-rotate-left"></i> Restablecer</button>
    </div>
  `));

  // HERO
  content.appendChild(elSection('s-hero', `
    <div class="grid md:grid-cols-2 gap-6">
      <div class="space-y-3">
        ${input('Marca', 'i-brand', state.site.brand)}
        ${input('Tagline', 'i-tagline', state.site.tagline)}
        ${input('Título (Hero)', 'i-hero-title', state.hero.title)}
        ${textarea('Subtítulo (Hero)', 'i-hero-subtitle', state.hero.subtitle)}
        ${input('Imagen (URL)', 'i-hero-image', state.hero.image)}
      </div>
      <div class="space-y-3">
        <h4 class="font-semibold">CTA Principal</h4>
        ${input('Etiqueta', 'i-cta1-label', state.hero.cta1.label)}
        ${input('Icono (clase FA)', 'i-cta1-icon', state.hero.cta1.icon)}
        ${input('URL', 'i-cta1-link', state.hero.cta1.link)}
        <h4 class="font-semibold mt-4">CTA Secundario</h4>
        ${input('Etiqueta', 'i-cta2-label', state.hero.cta2.label)}
        ${input('Icono (clase FA)', 'i-cta2-icon', state.hero.cta2.icon)}
        ${input('URL', 'i-cta2-link', state.hero.cta2.link)}
      </div>
    </div>
  `));

  // Servicios editor
  const servicesForms = state.services.map((s,i)=>`
    <div class="rounded-xl border p-4 dark:border-slate-800">
      ${input('Icono (clase FA)', `i-srv-icon-${i}`, s.icon)}
      ${input('Título', `i-srv-title-${i}`, s.title)}
      ${textarea('Descripción', `i-srv-desc-${i}`, s.desc)}
      ${textarea('Puntos (uno por línea)', `i-srv-pts-${i}`, s.points.join('\n'))}
      <div class="flex gap-2 mt-2">
        <button data-del-srv="${i}" class="text-red-600 hover:underline"><i class="fa-solid fa-trash mr-1"></i>Eliminar</button>
      </div>
    </div>`).join('');

  content.appendChild(elSection('s-servicios', `
    <div class="flex items-center justify-between mb-3">
      <p class="text-slate-600">Gestiona las tarjetas visibles en la landing.</p>
      <button id="btn-add-srv" class="rounded-xl bg-primary-600 px-3 py-2 text-white"><i class="fa-solid fa-plus mr-1"></i>Agregar servicio</button>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">${servicesForms}</div>
  `));

  // Marcas
  const logos = state.partners.map((src,i)=>`
    <div class="border-2 border-dashed rounded-xl p-4 flex flex-col items-center gap-3">
      <img src="${src}" class="h-10 object-contain" alt="logo"/>
      ${input('URL del logo', `i-logo-${i}`, src)}
      <button data-del-logo="${i}" class="text-red-600 hover:underline"><i class="fa-solid fa-trash mr-1"></i>Eliminar</button>
    </div>`).join('');
  content.appendChild(elSection('s-marcas', `
    <div class="flex items-center justify-between mb-3">
      <p class="text-slate-600">Logos de partners mostrados en carrusel.</p>
      <button id="btn-add-logo" class="rounded-xl bg-primary-600 px-3 py-2 text-white"><i class="fa-solid fa-plus mr-1"></i>Agregar logo</button>
    </div>
    <div class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">${logos}</div>
  `));

  // Showroom
  content.appendChild(elSection('s-showroom', `
    ${input('URL de reserva', 'i-showroom-url', state.showroom.url)}
    ${input('Imagen (URL)', 'i-showroom-img', state.showroom.image)}
    ${textarea('Descripción', 'i-showroom-blurb', state.showroom.blurb)}
  `));

  // Proyectos
  const projs = state.projects.map((p,i)=>`
    <div class="border rounded-xl p-4 dark:border-slate-800">
      ${input('Título', `i-prj-title-${i}`, p.title)}
      ${textarea('Descripción', `i-prj-desc-${i}`, p.desc)}
      ${input('Imagen (URL)', `i-prj-img-${i}`, p.image)}
      <div class="flex gap-2 mt-2">
        <button data-del-prj="${i}" class="text-red-600 hover:underline"><i class="fa-solid fa-trash mr-1"></i>Eliminar</button>
      </div>
    </div>`).join('');
  content.appendChild(elSection('s-proyectos', `
    <div class="flex items-center justify-between mb-3">
      <p class="text-slate-600">Casos o proyectos destacados.</p>
      <button id="btn-add-prj" class="rounded-xl bg-primary-600 px-3 py-2 text-white"><i class="fa-solid fa-plus mr-1"></i>Agregar proyecto</button>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">${projs}</div>
  `));

  // Contacto
  content.appendChild(elSection('s-contacto', `
    ${input('Teléfono mostrado', 'i-phone', state.contact.phoneFormatted)}
    ${input('Email mostrado', 'i-email', state.contact.email)}
    ${input('WhatsApp (solo números)', 'i-wa', state.contact.whatsapp)}
    ${textarea('Mensaje WhatsApp', 'i-wa-msg', state.contact.whatsMsg)}
  `));

  // Links
  content.appendChild(elSection('s-links', `
    ${input('Showroom URL', 'i-link-showroom', state.links.showroom)}
    ${input('Facebook', 'i-link-facebook', state.links.facebook)}
    ${input('Instagram', 'i-link-instagram', state.links.instagram)}
    ${input('LinkedIn', 'i-link-linkedin', state.links.linkedin)}
    ${input('YouTube', 'i-link-youtube', state.links.youtube)}
    <div class="mt-4">
      <a href="${whatsAppURL(state)}" target="_blank" class="inline-flex items-center gap-2 rounded-xl border px-3 py-2 hover:bg-slate-50 dark:hover:bg-slate-800"><i class="fa-brands fa-whatsapp"></i> Probar WhatsApp</a>
    </div>
  `));

  // Tema
  content.appendChild(elSection('s-tema', `
    <div class="grid md:grid-cols-3 gap-4">
      <div class="rounded-xl border p-4 dark:border-slate-800">
        <p class="text-sm font-semibold">Modo</p>
        <div class="mt-2 flex gap-2">
          <button data-mode="light" class="rounded-xl border px-3 py-2 hover:bg-slate-50 dark:hover:bg-slate-800">Claro</button>
          <button data-mode="dark" class="rounded-xl border px-3 py-2 hover:bg-slate-50 dark:hover:bg-slate-800">Oscuro</button>
          <button data-mode="system" class="rounded-xl border px-3 py-2 hover:bg-slate-50 dark:hover:bg-slate-800">Automático</button>
        </div>
      </div>
      <div class="rounded-xl border p-4 dark:border-slate-800">
        ${input('Color primario (hex)', 'i-primary', state.theme.primary)}
        ${input('Color acento (hex)', 'i-accent', state.theme.accent)}
      </div>
      <div class="rounded-xl border p-4 dark:border-slate-800">
        <button id="btn-reset-theme" class="w-full rounded-xl bg-slate-900 px-4 py-2 text-white dark:bg-slate-700">Restablecer tema</button>
      </div>
    </div>
  `));

  bind();
}

function elSection(id, inner){
  const wrap = document.createElement('section');
  wrap.id = id;
  wrap.className = 'bg-white dark:bg-slate-900 rounded-2xl shadow-soft p-6 border border-slate-200 dark:border-slate-800';
  wrap.innerHTML = `<h3 class="text-xl font-bold mb-4">${sections.find(s=>s.id===id)?.label || ''}</h3>${inner}`;
  return wrap;
}
function input(label, id, val=''){ return `<label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">${label}</label><input id="${id}" value="${val??''}" class="mb-4 w-full rounded-xl border px-3 py-2 dark:border-slate-700 dark:bg-slate-800">`; }
function textarea(label, id, val=''){ return `<label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">${label}</label><textarea id="${id}" rows="3" class="mb-4 w-full rounded-xl border px-3 py-2 dark:border-slate-700 dark:bg-slate-800">${val??''}</textarea>`; }

function bind(){
  // Sidebar active state
  $$('.sidebar-link').forEach(a => {
    a.addEventListener('click', e => {
      $$('.sidebar-link').forEach(l => l.classList.remove('active-link'));
      a.classList.add('active-link');
      const target = a.getAttribute('href') || '#s-dashboard';
      const el = document.querySelector(target);
      if (el) el.scrollIntoView({ behavior:'smooth', block:'start' });
      e.preventDefault();
    });
  });

  // Collapse
  $('#btn-collapse').addEventListener('click', ()=>{
    const sidebar = $('#sidebar');
    sidebar.classList.toggle('sidebar-collapsed');
  });

  // Theme toggle icon in header
  $('#btn-theme').addEventListener('click', ()=>{
    state.theme.mode = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
    applyTheme(state);
    saveState(state);
    $('#i-theme').className = document.documentElement.classList.contains('dark') ? 'fa-solid fa-sun text-lg' : 'fa-solid fa-moon text-lg';
  });

  // Export / Import / Reset
  $('#btn-export').addEventListener('click', ()=>{
    const blob = new Blob([JSON.stringify(state, null, 2)], {type:'application/json'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'ac_site_config.json';
    a.click();
    URL.revokeObjectURL(a.href);
  });
  $('#file-import').addEventListener('change', (e)=>{
    const file = e.target.files?.[0];
    if(!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try{
        const data = JSON.parse(reader.result);
        state = Object.assign(state, data);
        saveState(state);
        build();
      }catch(err){ alert('JSON inválido'); }
    };
    reader.readAsText(file);
  });
  $('#btn-reset-all').addEventListener('click', ()=>{
    if(confirm('¿Restablecer todo el contenido a valores por defecto?')){
      state = resetState();
      saveState(state);
      build();
    }
  });

  // HERO bindings
  onInput('i-brand', v => state.site.brand = v);
  onInput('i-tagline', v => state.site.tagline = v);
  onInput('i-hero-title', v => state.hero.title = v);
  onInput('i-hero-subtitle', v => state.hero.subtitle = v);
  onInput('i-hero-image', v => state.hero.image = v);
  onInput('i-cta1-label', v => state.hero.cta1.label = v);
  onInput('i-cta1-icon', v => state.hero.cta1.icon = v);
  onInput('i-cta1-link', v => state.hero.cta1.link = v);
  onInput('i-cta2-label', v => state.hero.cta2.label = v);
  onInput('i-cta2-icon', v => state.hero.cta2.icon = v);
  onInput('i-cta2-link', v => state.hero.cta2.link = v);

  // Servicios
  $('#btn-add-srv').addEventListener('click', ()=>{
    state.services.push({ icon:'fa-solid fa-circle', title:'Nuevo servicio', desc:'Descripción...', points:['Punto 1','Punto 2'] });
    saveState(state); build();
  });
  $("[id^='s-servicios']").addEventListener('click', (e)=>{
    const del = e.target.closest('[data-del-srv]');
    if(del){
      const i = +del.getAttribute('data-del-srv');
      state.services.splice(i,1);
      saveState(state); build();
    }
  });
  state.services.forEach((s,i)=>{
    onInput(`i-srv-icon-${i}`, v => s.icon = v);
    onInput(`i-srv-title-${i}`, v => s.title = v);
    onInput(`i-srv-desc-${i}`, v => s.desc = v);
    onInput(`i-srv-pts-${i}`, v => s.points = v.split('\n').map(x=>x.trim()).filter(Boolean));
  });

  // Marcas
  $('#btn-add-logo').addEventListener('click', ()=>{
    state.partners.push('https://upload.wikimedia.org/wikipedia/commons/4/44/Logitech_logo.svg');
    saveState(state); build();
  });
  $("[id^='s-marcas']").addEventListener('click', (e)=>{
    const del = e.target.closest('[data-del-logo]');
    if(del){
      const i = +del.getAttribute('data-del-logo');
      state.partners.splice(i,1);
      saveState(state); build();
    }
  });
  state.partners.forEach((src,i)=> onInput(`i-logo-${i}`, v => state.partners[i] = v));

  // Showroom
  onInput('i-showroom-url', v => state.showroom.url = v);
  onInput('i-showroom-img', v => state.showroom.image = v);
  onInput('i-showroom-blurb', v => state.showroom.blurb = v);

  // Proyectos
  $('#btn-add-prj').addEventListener('click', ()=>{
    state.projects.push({ title:'Nuevo proyecto', desc:'Descripción...', image:'https://images.unsplash.com/photo-1542744173-05336fcc7ad4?q=80&w=1600&auto=format&fit=crop' });
    saveState(state); build();
  });
  $("[id^='s-proyectos']").addEventListener('click', (e)=>{
    const del = e.target.closest('[data-del-prj]');
    if(del){
      const i = +del.getAttribute('data-del-prj');
      state.projects.splice(i,1);
      saveState(state); build();
    }
  });
  state.projects.forEach((p,i)=>{
    onInput(`i-prj-title-${i}`, v => p.title = v);
    onInput(`i-prj-desc-${i}`, v => p.desc = v);
    onInput(`i-prj-img-${i}`, v => p.image = v);
  });

  // Contacto
  onInput('i-phone', v => state.contact.phoneFormatted = v);
  onInput('i-email', v => state.contact.email = v);
  onInput('i-wa', v => state.contact.whatsapp = v.replace(/\D+/g,''));
  onInput('i-wa-msg', v => state.contact.whatsMsg = v);

  // Links
  onInput('i-link-showroom', v => state.links.showroom = v);
  onInput('i-link-facebook', v => state.links.facebook = v);
  onInput('i-link-instagram', v => state.links.instagram = v);
  onInput('i-link-linkedin', v => state.links.linkedin = v);
  onInput('i-link-youtube', v => state.links.youtube = v);

  // Tema
  $$("[data-mode]").forEach(b => b.addEventListener('click', ()=>{
    state.theme.mode = b.getAttribute('data-mode');
    applyTheme(state);
    saveState(state);
    $('#i-theme').className = document.documentElement.classList.contains('dark') ? 'fa-solid fa-sun text-lg' : 'fa-solid fa-moon text-lg';
  }));
  onInput('i-primary', v => { state.theme.primary = v; applyTheme(state); });
  onInput('i-accent', v => { state.theme.accent = v; document.documentElement.style.setProperty('--color-accent', v); saveState(state); });
  $('#btn-reset-theme').addEventListener('click', ()=>{
    state.theme = structuredClone(initialState.theme);
    applyTheme(state); saveState(state); build();
  });
}

function onInput(id, fn){
  const el = document.getElementById(id);
  if(!el) return;
  el.addEventListener('input', (e)=>{
    fn(e.target.value);
    saveState(state);
  });
}

(function init(){
  build();
  // respond to changes from Landing if open in another tab
  window.addEventListener('storage', (e)=>{
    if(e.key === 'ac_suite_cms_v1'){
      state = loadState();
      build();
    }
  });
})();