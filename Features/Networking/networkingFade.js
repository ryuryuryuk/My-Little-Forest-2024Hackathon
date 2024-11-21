// 이미지 배열
const arrayIMG = document.querySelectorAll('.animation-fade');

var current = 0;

// fade 효과를 주는 함수
function changeImage() {
    // 모든 이미지의 'active' 클래스를 제거
    arrayIMG.forEach((img) => {
        img.classList.remove('active');
    });

    // 현재 이미지를 'active' 클래스를 추가해 표시
    arrayIMG[current].classList.add('active');

    // 다음 이미지로 이동
    current = (current + 1) % arrayIMG.length;
}

// 2초마다 이미지 변경
setInterval(changeImage, 2000);
