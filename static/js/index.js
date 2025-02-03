const chirpTextArea = document.querySelector('.form__post-content')
const chirpCounter = document.querySelector('.form__post-counter');

chirpTextArea.addEventListener('input', (e) => {
  const characterCount = e.target.value.length;
  chirpCounter.style.color = characterCount === 250 ? "red" : "var(--clr-accent)";
  chirpCounter.innerHTML = characterCount;
})