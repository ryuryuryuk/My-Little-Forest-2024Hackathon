document.getElementById("search-button").addEventListener("click", () => {
    const input = document.getElementById("search-input").value.toLowerCase(); 
    const boxes = document.querySelectorAll(".site-img"); 
    const noResultsMessage = document.querySelector(".no-results");  // "해당 그룹이 없어요" 메시지
    const slideButtons = document.querySelectorAll(".slide");  // 슬라이드 버튼들
    const siteContainer = document.querySelector(".site-container"); // 사이트 이미지들을 감싸는 컨테이너
    let visibleCount = 0; // 보여지는 박스 개수

    // 검색 입력이 없을 때 초기 상태로 돌아가기
    if (!input) {
        let count = 0;
        // 모든 박스를 숨기고 최대 3개만 보이게 처리
        boxes.forEach(box => {
            if (count < 3) {
                box.style.display = "block"; // 최대 3개는 보이게
                count++;
            } else {
                box.style.display = "none"; // 3개 초과는 숨기기
            }
        });

        // 슬라이드 버튼 표시
        noResultsMessage.style.display = "none";  // 결과 메시지 숨기기
        slideButtons.forEach(button => button.style.display = "block");  // 슬라이드 버튼 보이기
        siteContainer.style.transform = "translateX(0)"; // 초기 슬라이드 위치로 되돌리기

        return; // 검색이 없으면 여기서 종료
    }

    // 검색 입력이 있을 때
    boxes.forEach(box => {
        const tag = box.dataset.tag.toLowerCase(); 
        if (tag.includes(input)) {
            box.style.display = "block";
            visibleCount++; // 해당 태그가 포함되면 visibleCount 증가
        } else {
            box.style.display = "none"; 
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
