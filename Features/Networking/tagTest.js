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

        // 검색어로 필터링
        filteredImages = Array.from(siteImages).filter(img => {
            const tags = img.dataset.tag.split(' ');
            return tags.includes(searchValue);
        });

        // 결과 처리
        if (filteredImages.length > 0) {
            noResults.style.display = 'none'; // "결과 없음" 숨기기
            updateSlide(); // 슬라이드 갱신
        } else {
            noResults.style.display = 'block'; // "결과 없음" 표시
            siteImages.forEach(img => img.style.display = 'none'); // 모든 이미지 숨기기
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
