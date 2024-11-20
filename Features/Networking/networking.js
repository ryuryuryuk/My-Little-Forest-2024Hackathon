document.addEventListener("DOMContentLoaded", function () {
    var images = document.querySelectorAll('.animation-fade');
     let currentIndex = 0;

    function changeImage() {
         images[currentIndex].classList.remove('active'); //class를 제거한다
            
        currentIndex = (currentIndex + 1) % images.length; 
        images[currentIndex].classList.add('active'); //class를 부여한다
    }

    setInterval(changeImage, 2000);
});
