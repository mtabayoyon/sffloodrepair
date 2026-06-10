// Nav toggle
(function(){
  var t = document.getElementById('nt');
  var n = document.getElementById('mn');
  if(!t || !n) return;

  t.addEventListener('click', function(e){
    e.stopPropagation();
    var isOpen = n.classList.toggle('open');
    t.setAttribute('aria-expanded', isOpen);
    // Animate hamburger to X
    var spans = t.querySelectorAll('span');
    if(isOpen){
      spans[0].style.transform = 'rotate(45deg) translate(5px,5px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px,-5px)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  });

  // Close when clicking outside
  document.addEventListener('click', function(e){
    if(!n.contains(e.target) && !t.contains(e.target)){
      n.classList.remove('open');
      t.setAttribute('aria-expanded','false');
      t.querySelectorAll('span').forEach(function(s){ s.style.transform=''; s.style.opacity=''; });
    }
  });

  // Close when a nav link is clicked
  n.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){
      n.classList.remove('open');
      t.setAttribute('aria-expanded','false');
      t.querySelectorAll('span').forEach(function(s){ s.style.transform=''; s.style.opacity=''; });
    });
  });
})();

// FAQ accordion
document.querySelectorAll('.fq').forEach(function(b){
  b.addEventListener('click',function(){
    var a=this.nextElementSibling, o=this.classList.contains('open');
    document.querySelectorAll('.fq').forEach(function(x){
      x.classList.remove('open');
      x.setAttribute('aria-expanded','false');
      if(x.nextElementSibling) x.nextElementSibling.classList.remove('open');
    });
    if(!o){
      this.classList.add('open');
      this.setAttribute('aria-expanded','true');
      if(a) a.classList.add('open');
    }
  });
});

// Fade-up animations on scroll
if(window.IntersectionObserver){
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(x){
      if(x.isIntersecting){ x.target.style.animationPlayState='running'; obs.unobserve(x.target); }
    });
  },{threshold:0.1});
  document.querySelectorAll('.fu').forEach(function(el){
    el.style.animationPlayState='paused'; obs.observe(el);
  });
}

// Contact form — Formspree → dispatch@teamallied.co
var cf = document.getElementById('contact-form');
if(cf){
  cf.addEventListener('submit', function(e){
    e.preventDefault();
    var btn = cf.querySelector('.bsub');
    var originalText = btn.textContent;
    btn.textContent = 'Sending...';
    btn.disabled = true;
    var formData = new FormData(cf);
    fetch('https://formspree.io/f/xpwzgvqk',{
      method:'POST', body:formData, headers:{'Accept':'application/json'}
    }).then(function(r){
      if(r.ok){
        btn.textContent = "✓ Message Sent! We'll call you within 30 minutes.";
        btn.style.background = '#008000';
        cf.reset();
      } else {
        throw new Error('failed');
      }
    }).catch(function(){
      var name = (formData.get('first_name')||'') + ' ' + (formData.get('last_name')||'');
      var subject = encodeURIComponent('New Service Request — ' + name.trim());
      var body = encodeURIComponent('Name: '+name+'\nPhone: '+(formData.get('phone')||'')+'\nAddress: '+(formData.get('address')||'')+'\nService: '+(formData.get('service')||'')+'\nDescription: '+(formData.get('description')||''));
      window.location.href = 'mailto:dispatch@teamallied.co?subject='+subject+'&body='+body;
      setTimeout(function(){ btn.textContent=originalText; btn.disabled=false; btn.style.background=''; }, 3000);
    });
  });
}
