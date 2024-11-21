// 이미지 배열
const images = document.querySelectorAll('.animation-fade');

var currentIndex = 0;

// fade 효과를 주는 함수
function changeImage() {
    // 모든 이미지의 'active' 클래스를 제거
    images.forEach((img) => {
        img.classList.remove('active');
    });

    // 현재 이미지를 'active' 클래스를 추가해 표시
    images[currentIndex].classList.add('active');

    // 다음 이미지로 이동
    currentIndex = (currentIndex + 1) % images.length;
}

// 2초마다 이미지 변경
setInterval(changeImage, 2000);
