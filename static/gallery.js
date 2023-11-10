let slideIndex = 0;
let slideTimeout;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active-dot", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active-dot";
    
    // Clear existing timeout
  if (slideTimeout) {
    clearTimeout(slideTimeout);
  }

  // Set new timeout
  slideTimeout = setTimeout(showSlides, 5000);
}

// Thumbnail image controls
function currentSlide(n) {
    slideIndex = n-1;
    showSlides();
  }

  // Add event listeners to the dots
let dotElements = document.getElementsByClassName("dot");
for (let i = 0; i < dotElements.length; i++) {
  dotElements[i].addEventListener("click", function() {
    currentSlide(i + 1); // Slide index is 1-based
  });
}
