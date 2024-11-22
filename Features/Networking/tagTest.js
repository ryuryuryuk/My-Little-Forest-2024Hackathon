document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const siteImages = document.querySelectorAll('.site-img');
    const noResults = document.querySelector('.no-results');
    const leftButton = document.querySelector('.slide.left');
    const rightButton = document.querySelector('.slide.right');

    let filteredImages = Array.from(siteImages); // 현재 표시 중인 이미지 (초기에는 전체)
    let currentIndex = 0; // 현재 첫 번째로 표시 중인 이미지의 인덱스
    const imagesPerPage = 3; // 한 번에 보여줄 이미지 수

    // 슬라이드 업데이트 함수
    function updateSlide() {
        // 모든 이미지를 숨기고, 현재 인덱스에 따라 3개의 이미지만 표시
        siteImages.forEach(img => img.style.display = 'none');
        for (let i = 0; i < imagesPerPage; i++) {
            const index = currentIndex + i;
            if (filteredImages[index]) {
                filteredImages[index].style.display = 'block';
            }
        }
    }

    // 검색 기능
    searchButton.addEventListener('click', () => {
        const searchValue = searchInput.value.trim();
        currentIndex = 0; // 검색 후 첫 번째 이미지부터 시작

        if (!searchValue) {
            // 검색어가 공백일 경우 초기 화면 표시
            filteredImages = Array.from(siteImages);
            noResults.style.display = 'none'; // "결과 없음" 숨기기
            leftButton.style.display = 'block'; // 버튼 복원
            rightButton.style.display = 'block';
            updateSlide(); // 초기 화면 갱신
            return;
        }

        // 검색어로 필터링
        filteredImages = Array.from(siteImages).filter(img => {
            const tags = img.dataset.tag.split(' ');
            return tags.includes(searchValue);
        });

        // 결과 처리
        if (filteredImages.length > 0) {
            noResults.style.display = 'none'; // "결과 없음" 숨기기
            leftButton.style.display = 'block'; // 버튼 복원
            rightButton.style.display = 'block';
            updateSlide(); // 슬라이드 갱신
        } else {
            noResults.style.display = 'block'; // "결과 없음" 표시
            siteImages.forEach(img => img.style.display = 'none'); // 모든 이미지 숨기기
            leftButton.style.display = 'none'; // 버튼 삭제
            rightButton.style.display = 'none'; // 버튼 삭제
        }
    });

    // 이전 버튼 기능
    leftButton.addEventListener('click', () => {
        if (filteredImages.length > 0) {
            currentIndex = Math.max(currentIndex - imagesPerPage, 0); // 인덱스 감소, 최소 0
            updateSlide();
        }
    });

    // 다음 버튼 기능
    rightButton.addEventListener('click', () => {
        if (filteredImages.length > 0) {
            currentIndex = Math.min(currentIndex + imagesPerPage, filteredImages.length - imagesPerPage); // 인덱스 증가, 최대 (마지막 페이지 시작점)
            updateSlide();
        }
    });

    // 초기화
    updateSlide();
});

/*
추가한 기능
1. 검색창에 "아무것도 입력하지 않았을 경우" 처음 화면을 출력함
2. 검색창에 입력한 tag와 일치하는 tag가 없는 경우 noResults를 출력하되, leftButton와 rightButton을 삭제함
*/ 