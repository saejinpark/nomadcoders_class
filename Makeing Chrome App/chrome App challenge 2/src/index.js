const backgroundColorSwiper = () => {
  const width = window.innerWidth;
  const body = document.querySelector("body");
  if (width < 800) {
    body.style.backgroundColor = "#448AFF";
  } else if (width < 1200) {
    body.style.backgroundColor = "#E040FB";
  } else {
    body.style.backgroundColor = "#FFC107";
  }
};

backgroundColorSwiper();
window.addEventListener("resize", backgroundColorSwiper);
