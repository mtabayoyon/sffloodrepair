// Nav toggle
(function(){var t=document.getElementById('nt'),n=document.getElementById('mn');if(!t||!n)return;t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});document.addEventListener('click',function(e){if(!n.contains(e.target)&&!t.contains(e.target)){n.classList.remove('open');t.setAttribute('aria-expanded','false')}})})();

// FAQ accordion
document.querySelectorAll('.fq').forEach(function(b){b.addEventListener('click',function(){var a=this.nextElementSibling,o=this.classList.contains('open');document.querySelectorAll('.fq').forEach(function(x){x.classList.remove('open');x.setAttribute('aria-expanded','false');if(x.nextElementSibling)x.nextElementSibling.classList.remove('open')});if(!o){this.classList.add('open');this.setAttribute('aria-expanded','true');if(a)a.classList.add('open')}})});

// Fade-up animations
if(window.IntersectionObserver){var obs=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.style.animationPlayState='running';obs.unobserve(x.target)}})},{threshold:0.1});document.querySelectorAll('.fu').forEach(function(el){el.style.animationPlayState='paused';obs.observe(el)})}

// Contact form — submits to Formspree → forwards to dispatch@teamallied.co
var cf = document.getElementById('contact-form');
if(cf){
  cf.addEventListener('submit', function(e){
    e.preventDefault();
    var btn = cf.querySelector('.bsub');
    var originalText = btn.textContent;
    btn.textContent = 'Sending...';
    btn.disabled = true;

    var formData = new FormData(cf);

    fetch('https://formspree.io/f/xpwzgvqk', {
      method: 'POST',
      body: formData,
      headers: { 'Accept': 'application/json' }
    })
    .then(function(response){
      if(response.ok){
        btn.textContent = '✓ Message Sent! We'll call you within 30 minutes.';
        btn.style.background = '#008000';
        cf.reset();
      } else {
        return response.json().then(function(data){
          throw new Error(data.error || 'Form submission failed');
        });
      }
    })
    .catch(function(error){
      // Fallback: open email client directly
      var name = formData.get('first_name') + ' ' + formData.get('last_name');
      var phone = formData.get('phone') || '';
      var address = formData.get('address') || '';
      var service = formData.get('service') || '';
      var desc = formData.get('description') || '';
      var subject = encodeURIComponent('New Service Request — ' + name);
      var body = encodeURIComponent(
        'Name: ' + name + '\n' +
        'Phone: ' + phone + '\n' +
        'Address: ' + address + '\n' +
        'Service Type: ' + service + '\n' +
        'Description: ' + desc
      );
      window.location.href = 'mailto:dispatch@teamallied.co?subject=' + subject + '&body=' + body;
      btn.textContent = 'Opening email client...';
      btn.style.background = 'var(--blue)';
      setTimeout(function(){ btn.textContent = originalText; btn.disabled = false; btn.style.background = ''; }, 3000);
    });
  });
}
