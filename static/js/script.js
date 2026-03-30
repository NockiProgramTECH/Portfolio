

  // ── Année dynamique ──────────────────────────────────────────
  document.getElementById('year').textContent = new Date().getFullYear();

  // ── Navbar scroll ────────────────────────────────────────────
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  // ── Mobile menu ──────────────────────────────────────────────
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileClose = document.getElementById('mobileClose');

  function openMobile() {
    mobileMenu.classList.add('open');
    hamburger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }
  function closeMobile() {
    mobileMenu.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  hamburger.addEventListener('click', openMobile);
  mobileClose.addEventListener('click', closeMobile);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeMobile();
  });

  // ── Scroll reveal ────────────────────────────────────────────
  const revealEls = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  revealEls.forEach(el => observer.observe(el));

  // ── Active nav link ──────────────────────────────────────────
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');
  const activeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.style.color = link.getAttribute('href') === '#' + entry.target.id
            ? 'var(--text)' : '';
        });
      }
    });
  }, { threshold: 0.4 });
  sections.forEach(s => activeObserver.observe(s));

  // ── Contact form AJAX vers Django ─────────────────────────────
  function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split(';') : [];
    for (const cookie of cookies) {
      const [k, v] = cookie.trim().split('=');
      if (k === name) {
        return decodeURIComponent(v);
      }
    }
    return null;
  }

  const contactForm = document.getElementById('contactForm');
  const status = document.getElementById('form-status');
  const csrftoken = getCookie('csrftoken');

  contactForm.addEventListener('submit', e => {
    e.preventDefault();

    const btn = contactForm.querySelector('button[type=submit]');
    btn.disabled = true;
    btn.textContent = 'Envoi en cours…';

    fetch(contactForm.action, {
      method: 'POST',
      body: new FormData(contactForm),
      headers: {
        'X-CSRFToken': csrftoken,
        'Accept': 'application/json',
      },
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw err; });
      }
      return response.json();
    })
    .then(data => {
      status.style.display = 'block';
      status.textContent = data.message || '✓ Message envoyé avec succès !';
      status.style.color = 'var(--accent)';
      contactForm.reset();
    })
    .catch(err => {
      status.style.display = 'block';
      status.textContent = err.error || '✗ Une erreur est survenue. Veuillez réessayer.';
      status.style.color = '#e74c3c';
    })
    .finally(() => {
      btn.disabled = false;
      btn.innerHTML = 'Envoyer le message <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>';
    });
  });

