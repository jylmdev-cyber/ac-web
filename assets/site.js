import { $, $$, initialState, loadState, saveState, applyTheme, whatsAppURL } from './cms.js';

async function loadPartials(){
  $('#header').innerHTML = await (await fetch('./components/header.html')).text();
  $('#inicio').innerHTML  = await (await fetch('./sections/hero.html')).text();
  $('#servicios').innerHTML = await (await fetch('./sections/servicios.html')).text();
  $('#marcas').innerHTML = await (await fetch('./sections/marcas.html')).text();
  $('#showroom').innerHTML = await (await fetch('./sections/showroom.html')).text();
  $('#proyectos').innerHTML = await (await fetch('./sections/proyectos.html')).text();
  $('#contacto').innerHTML = await (await fetch('./sections/contacto.html')).text();
  $('#footer').innerHTML = await (await fetch('./components/footer.html')).text();
}

function render(state){
  // Apply theme & tokens
  applyTheme(state);

  // Header text
  $('#site-title').textContent = state.site.title;
  $('#brand').textContent = state.site.brand;
  $('#brand-foot').textContent = state.site.brand;
  $('#tagline').textContent = state.site.tagline;

  // Hero
  $('#hero-title').textContent = state.hero.title;
  $('#hero-subtitle').textContent = state.hero.subtitle;
  $('#hero-image').src = state.hero.image;
  $('#cta-1-label').textContent = state.hero.cta1.label;
  $('#cta-1').href = state.hero.cta1.link || '#';
  $('#cta-1-icon').className = state.hero.cta1.icon || 'fa-solid fa-bolt';
  $('#cta-2-label').textContent = state.hero.cta2.label;
  $('#cta-2').href = state.hero.cta2.link || '#';
  $('#cta-2-icon').className = state.hero.cta2.icon || 'fa-brands fa-whatsapp';

  // Servicios
  const grid = $('#services-grid');
  grid.innerHTML = '';
  state.services.forEach(card => {
    const el = document.createElement('div');
    el.className = 'group rounded-2xl border p-6 shadow-soft transition hover:-translate-y-1 hover:shadow-lg dark:border-slate-800';
    el.innerHTML = `
      <div class="mb-3 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-primary-50 text-primary-700 group-hover:bg-primary-100">
        <i class="${card.icon}"></i>
      </div>
      <h3 class="font-semibold text-lg">${card.title}</h3>
      <p class="mt-2 text-sm text-slate-600 dark:text-slate-400">${card.desc}</p>
      <ul class="mt-4 space-y-1 text-sm text-slate-600 dark:text-slate-400">
        ${card.points.map(pt => `<li class="flex items-start gap-2"><i class="fa-solid fa-check mt-1 text-primary-600"></i><span>${pt}</span></li>`).join('')}
      </ul>`;
    grid.appendChild(el);
  });

  // Partners
  const row = $('#partners-row');
  row.innerHTML = '';
  state.partners.forEach(src => {
    const box = document.createElement('div');
    box.className = 'inline-flex h-16 min-w-[140px] items-center justify-center rounded-xl bg-white px-6 ring-1 ring-slate-200 dark:bg-slate-900 dark:ring-slate-800';
    box.innerHTML = `<img src="${src}" class="h-10 object-contain" alt="Marca"/>`;
    row.appendChild(box);
  });

  // Showroom
  $('#link-showroom').href = state.showroom.url || '#';
  $('#showroom-image').src = state.showroom.image;
  $('#showroom-blurb').textContent = state.showroom.blurb;

  // Projects
  const pgrid = $('#projects-grid');
  pgrid.innerHTML = '';
  state.projects.forEach(p => {
    const fig = document.createElement('figure');
    fig.className = 'group overflow-hidden rounded-2xl border shadow-soft transition hover:-translate-y-1 hover:shadow-lg dark:border-slate-800';
    fig.innerHTML = `
      <img src="${p.image}" alt="${p.title}" class="h-48 w-full object-cover transition group-hover:scale-105"/>
      <figcaption class="p-5">
        <h3 class="font-semibold">${p.title}</h3>
        <p class="mt-1 text-sm text-slate-600 dark:text-slate-400">${p.desc}</p>
      </figcaption>`;
    pgrid.appendChild(fig);
  });

  // Contact
  $('#contact-phone').textContent = state.contact.phoneFormatted;
  $('#contact-email').textContent = state.contact.email;

  // Footer links
  $('#link-facebook').href = state.links.facebook || '#';
  $('#link-instagram').href = state.links.instagram || '#';
  $('#link-linkedin').href = state.links.linkedin || '#';
  $('#link-youtube').href = state.links.youtube || '#';

  // WhatsApp FAB
  $('#wa-fab').href = whatsAppURL(state);

  // Header interactions
  $('#mobile-menu-btn').addEventListener('click', ()=> $('#mobile-menu').classList.toggle('hidden'));
  $('#theme-toggle').addEventListener('click', ()=>{
    state.theme.mode = state.theme.mode === 'dark' ? 'light' : 'dark';
    render(state);
    saveState(state);
  });
  const prefers = window.matchMedia('(prefers-color-scheme: dark)');
  prefers.onchange = ()=>{ if(state.theme.mode==='system'){ render(state); } };
  const icon = $('#theme-icon');
  if (icon) icon.className = (document.documentElement.classList.contains('dark')) ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
}

(async function init(){
  await loadPartials();
  let state = loadState();
  render(state);
  // Listen to external changes (admin)
  window.addEventListener('storage', (e)=>{
    if(e.key === 'ac_suite_cms_v1'){
      state = loadState();
      render(state);
    }
  });
})();