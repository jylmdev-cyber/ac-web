// assets/cms.js
// Single source of truth for site config across Landing (index.html) and Admin (admin.html)
export const STORAGE_KEY = 'ac_suite_cms_v1';

export const initialState = {
  theme: {
    dark: false,
    mode: 'system',   // 'light' | 'dark' | 'system'
    primary: '#2a9dff',
    accent:  '#00c9b7'
  },
  site: {
    title: 'AC Technology — Soluciones Integrales',
    brand: 'AC Technology',
    tagline: 'Soluciones integrales: corporativo, educativo y residencial'
  },
  hero: {
    title: 'Proyectos INTEGRALES en tecnología',
    subtitle: 'Integramos soluciones de audio, video, redes, domótica y seguridad para empresas, instituciones educativas y residencias.',
    image: 'https://images.unsplash.com/photo-1518779578993-ec3579fee39f?q=80&w=1600&auto=format&fit=crop',
    cta1: { label:'Conoce el demo virtual', link:'https://www.figma.com/', icon:'fa-solid fa-bolt' },
    cta2: { label:'Escríbenos por WhatsApp', link:'#', icon:'fa-brands fa-whatsapp' }
  },
  services: [
    { icon:'fa-solid fa-network-wired', title:'Redes & Cableado Estructurado', desc:'Diseño e implementación de redes LAN/WiFi de alto rendimiento.', points:['Site survey','Switching & routing','WiFi empresarial'] },
    { icon:'fa-solid fa-video', title:'Audio/Video & Salas de Reunión', desc:'Videoconferencia, pantallas LED, sonido profesional y control.', points:['Zoom/Teams Rooms','Señalética digital','Matricería AV'] },
    { icon:'fa-solid fa-house-signal', title:'Domótica & Seguridad', desc:'CCTV, control de accesos, alarmas e integración IoT.', points:['Cámaras IP','Sensores & control','Automatización'] }
  ],
  partners: [
    'https://upload.wikimedia.org/wikipedia/commons/4/44/Logitech_logo.svg',
    'https://upload.wikimedia.org/wikipedia/commons/4/45/Dahua_Technology_logo.svg',
    'https://upload.wikimedia.org/wikipedia/commons/d/d3/Cisco_logo_blue_2016.svg',
    'https://upload.wikimedia.org/wikipedia/commons/1/14/Hikvision_logo.svg',
    'https://upload.wikimedia.org/wikipedia/commons/7/7f/Crestron_logo.svg',
    'https://upload.wikimedia.org/wikipedia/commons/6/6e/Yealink_logo.svg'
  ],
  showroom: {
    url: '#',
    image: 'https://images.unsplash.com/photo-1556761175-4b46a572b786?q=80&w=1600&auto=format&fit=crop',
    blurb: 'Equipado con lo último en tecnología. Agenda una demostración y recibe asesoría personalizada.'
  },
  projects: [
    { title:'Campus educativo — red WiFi y audiovisuales', desc:'Cobertura total, aulas híbridas y señalética digital.', image:'https://images.unsplash.com/photo-1587620962725-abab7fe55159?q=80&w=1600&auto=format&fit=crop' },
    { title:'Oficinas corporativas — salas de reunión', desc:'Videoconferencia certificada y control centralizado.', image:'https://images.unsplash.com/photo-1542744173-05336fcc7ad4?q=80&w=1600&auto=format&fit=crop' },
    { title:'Residencial premium — domótica y seguridad', desc:'Automatización, CCTV y audio multiroom.', image:'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?q=80&w=1600&auto=format&fit=crop' }
  ],
  contact: {
    phoneFormatted:'(+51) 01 543 1138',
    email:'informes@actechnology.com.pe',
    whatsapp:'51999999999',
    whatsMsg:'Hola, me gustaría más información sobre sus soluciones integrales.'
  },
  links: { showroom:'#', facebook:'#', instagram:'#', linkedin:'#', youtube:'#' }
};

export function loadState(){
  try{
    const raw = localStorage.getItem(STORAGE_KEY);
    if(!raw) return structuredClone(initialState);
    return Object.assign(structuredClone(initialState), JSON.parse(raw));
  }catch(e){
    return structuredClone(initialState);
  }
}

export function saveState(state){
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  // Notify other tabs/pages
  try { window.dispatchEvent(new StorageEvent('storage', { key: STORAGE_KEY, newValue: JSON.stringify(state) })); } catch {}
}

export function resetState(){
  localStorage.removeItem(STORAGE_KEY);
  return structuredClone(initialState);
}

// helpers
export const $ = (sel, root=document)=> root.querySelector(sel);
export const $$ = (sel, root=document)=> Array.from(root.querySelectorAll(sel));

export function applyTheme(state){
  const html = document.documentElement;
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const dark = state.theme.mode === 'dark' || (state.theme.mode === 'system' && prefersDark) || (state.theme.dark === true);
  html.classList.toggle('dark', !!dark);
  document.documentElement.style.setProperty('--color-primary', state.theme.primary);
}

// URL builders
export function whatsAppURL(state){
  const base = 'https://wa.me/' + (state.contact.whatsapp || '51999999999');
  const msg = encodeURIComponent(state.contact.whatsMsg || 'Hola, me gustaría más información.');
  return `${base}?text=${msg}`;
}
