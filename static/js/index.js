const chirpTextArea = document.querySelector('.form__post-content')
const chirpCounter = document.querySelector('.form__post-counter');

chirpTextArea.addEventListener('input', (e) => {
  const characterCount = e.target.value.length;
  chirpCounter.style.color = characterCount === 250 ? "red" : "var(--clr-accent)";
  chirpCounter.innerHTML = characterCount;
})


const posts = document.getElementsByClassName('post')

Array.from(posts).forEach(post => {
  if (post.dataset.liked === "true") {
    const postEngagement = post.children[1].children[2].children[0];
    const postLikeButton = postEngagement.children[1]
    const postLikeCounter = postEngagement.children[2]

    postLikeButton.children[0].classList.remove('bx-star')
    postLikeButton.children[0].classList.add('bxs-star')
    postLikeButton.children[0].style.color = "var(--clr-accent)"
    postLikeCounter.style.color = "var(--clr-accent)"
  }
})