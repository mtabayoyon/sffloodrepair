// Nav toggle
(function(){var t=document.getElementById('nt'),n=document.getElementById('mn');if(!t||!n)return;t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});document.addEventListener('click',function(e){if(!n.contains(e.target)&&!t.contains(e.target)){n.classList.remove('open');t.setAttribute('aria-expanded','false')}})})();
// FAQ
document.querySelectorAll('.fq').forEach(function(b){b.addEventListener('click',function(){var a=this.nextElementSibling,o=this.classList.contains('open');document.querySelectorAll('.fq').forEach(function(x){x.classList.remove('open');x.setAttribute('aria-expanded','false');if(x.nextElementSibling)x.nextElementSibling.classList.remove('open')});if(!o){this.classList.add('open');this.setAttribute('aria-expanded','true');if(a)a.classList.add('open')}})});
// Fade-up
if(window.IntersectionObserver){var obs=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.style.animationPlayState='running';obs.unobserve(x.target)}})},{threshold:0.1});document.querySelectorAll('.fu').forEach(function(el){el.style.animationPlayState='paused';obs.observe(el)})}
// Contact form
var cf=document.getElementById('contact-form');if(cf){cf.addEventListener('submit',function(e){e.preventDefault();var btn=cf.querySelector('.bsub');btn.textContent='✓ Message Sent! We\'ll call you within 30 minutes.';btn.style.background='#27ae60';btn.disabled=true})}
