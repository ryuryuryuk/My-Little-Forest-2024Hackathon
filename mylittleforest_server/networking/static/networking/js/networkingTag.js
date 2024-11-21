const searchButton = document.getElementById("search-button"); // 검색 버튼
const searchInput = document.getElementById("search-input"); // 검색 입력 필드
const leftSlideButton = document.querySelector('.slide.left');
const rightSlideButton = document.querySelector('.slide.right');
const images = document.querySelectorAll('.site-img');
const totalImages = images.length;  // 총 이미지 개수
const noResultsMessage = document.querySelector(".no-results");  // "해당 그룹이 없어요" 메시지
const slideButtons = document.querySelectorAll(".slide");  // 슬라이드 버튼들
const siteContainer = document.querySelector(".site-container"); // 사이트 이미지들을 감싸는 컨테이너
let currentIndex = 0;  // 현재 표시 중인 첫 번째 이미지 인덱스

// 이미지 표시 함수: 3개씩만 보이도록
function showImages() {
    images.forEach(img => { // 모든 이미지를 숨김
        img.classList.remove('visible'); // 보이는 이미지를 숨김
        img.classList.add('hidden');  // 숨겨진 상태로 변경
    });

    // 최대 3개의 이미지만 보이도록 설정
    for (let i = currentIndex; i < currentIndex + 3; i++) {  // 3개만 표시
        const index = i % totalImages;  // 이미지가 순환되도록
        images[index].classList.remove('hidden');  // 숨겨진 이미지를 표시
        images[index].classList.add('visible');  // 표시 상태로 변경
    }
}

// 이미지 크기 재조정 함수
function resizeImages() {
    images.forEach(image => {
        const imgElement = image.querySelector('img');
        if (imgElement) {
            imgElement.style.width = '100%';  // width를 100%로 설정하여 부모 컨테이너에 맞게 크기 조정
            imgElement.style.height = '100%';  // height도 100%로 설정하여 부모 컨테이너에 맞게 크기 조정
            imgElement.style.objectFit = 'cover';
        }
    });
}

// 왼쪽 버튼 클릭 시
leftSlideButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 3 + totalImages) % totalImages;  // 3개씩 왼쪽으로 이동
    showImages();
});

// 오른쪽 버튼 클릭 시
rightSlideButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 3) % totalImages;  // 3개씩 오른쪽으로 이동
    showImages();
});

// 검색 버튼 클릭 시
searchButton.addEventListener("click", () => {
    const input = searchInput.value.toLowerCase(); // 검색어를 소문자로 변환
    const boxes = document.querySelectorAll(".site-img"); // 이미지 박스
    let visibleCount = 0; // 보여지는 박스 개수

    // 검색 입력이 없을 때 초기 상태로 돌아가기
    if (!input) {
        let count = 0;
        // 모든 박스를 숨기고 최대 3개만 보이게 처리
        boxes.forEach(box => {
            box.classList.remove("hidden"); // 숨김 처리된 이미지 클래스를 제거
            if (count < 3) {
                box.classList.add("visible"); // 최대 3개는 보이게
                count++;
            } else {
                box.classList.add("hidden"); // 3개 초과는 숨기기
            }
        });

        // 슬라이드 버튼 표시
        noResultsMessage.style.display = "none";  // 결과 메시지 숨기기
        slideButtons.forEach(button => button.style.display = "block");  // 슬라이드 버튼 보이기
        siteContainer.style.transform = "translateX(0)"; // 초기 슬라이드 위치로 되돌리기
        currentIndex = 0; // 처음부터 시작
        showImages(); // 처음 3개 이미지 표시
        return; // 검색이 없으면 여기서 종료
    }

    // 검색 입력이 있을 때
    boxes.forEach(box => {
        const tag = box.dataset.tag.toLowerCase(); 
        if (tag.includes(input)) {
            box.classList.remove("hidden"); // 검색 결과에 맞는 이미지는 표시
            box.classList.add("visible");  // visible 클래스를 추가하여 표시
            visibleCount++; // 해당 태그가 포함되면 visibleCount 증가
        } else {
            box.classList.remove("visible");
            box.classList.add("hidden"); // 검색 결과에 맞지 않으면 숨기기
        }
    });

    // 검색 결과가 없을 때
    if (visibleCount === 0) {
        noResultsMessage.style.display = "block";  // 결과 없음 메시지 표시
        slideButtons.forEach(button => button.style.display = "none");  // 슬라이드 버튼 숨기기
        siteContainer.style.transform = "translateX(0)"; // 처음 위치로 되돌리기
    } else {
        noResultsMessage.style.display = "none";  // 결과가 있으면 메시지 숨기기
        // 3개 이하일 때는 슬라이드 버튼 숨기기
        if (visibleCount <= 3) {
            slideButtons.forEach(button => button.style.display = "none");  // 슬라이드 버튼 숨기기
        } else {
            slideButtons.forEach(button => button.style.display = "block");  // 슬라이드 버튼 표시
        }
    }
});

// 페이지가 처음 로드될 때 검색어가 없으면 초기 화면을 띄운다
document.addEventListener('DOMContentLoaded', function() {
    if (searchInput.value.trim() === '') {
        currentIndex = 0;  // 처음부터 시작
        showImages(); // 처음 3개 이미지 표시
    }
});