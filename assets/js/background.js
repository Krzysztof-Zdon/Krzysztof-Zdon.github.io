// Lista obrazów Van Gogha
const images = [
    "/assets/images/starry_night.jpg",
    "/assets/images/starry_night_city.jpg",
    "/assets/images/Wheat_Field_with_Crows.jpg"
];

let currentIndex = 0;

function changeBackground() {
    const background = document.querySelector('.background');
    background.style.backgroundImage = `url(${images[currentIndex]})`;

    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeBackground, 7000);

changeBackground();
