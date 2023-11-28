const element = document.querySelector('h2');

element.classList.add('typewriter');

setTimeout(() => {
  element.classList.remove('typewriter');
}, 2000);
