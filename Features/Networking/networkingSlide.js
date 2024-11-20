const leftSlideButton = document.querySelector('.slide.left');
const rightSlideButton = document.querySelector('.slide.right');
const images = document.querySelectorAll('.site-img'); 
const totalImages = images.length; // 반복 작업을 위해 이미지 총 개수 가져오기
let currentIndex = 0;

// 이미지 박스 개수가 많아 최대 한 화면에 3개까지만 보이도록 하기 위하여
function showImages() {
    images.forEach((img, index) => { // 모든 이미지를 숨김
        img.style.display = 'none';
    });

    for (let i = currentIndex; i < currentIndex + 3; i++) { // 한 화면에 3개의 이미지만 보이도록 
        if (images[i % totalImages]) { // 인덱스 순환을 한 조건문
            images[i % totalImages].style.display = 'inline-block'; // 화면에 보이게 되는 이미지 박스에다가는 display="inline-block" 속성 부여 >> 세 개를 나란히 배치
        }
    }
}

// 왼쪽 버튼 클릭했을 때
leftSlideButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 3 + totalImages) % totalImages; // 왼쪽으로 이동, 끝나면 첫 번째로 돌아감 >> 나머지로 구현
    showImages();
});

// 오른쪽 버튼 클릭했을 때
rightSlideButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 3) % totalImages; // 오른쪽으로 이동, 끝에 도달하면 처음으로 돌아감 >> 나머지로 구현
    showImages();
});

// 페이지가 로드되면, 해당 함수 호출: 이미지 3개만 표시
showImages();
