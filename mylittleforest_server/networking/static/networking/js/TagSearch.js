document.getElementById("search-button").addEventListener("click", () => {
    const input = document.getElementById("search-input").value.toLowerCase(); // 입력값 가져오기
    const boxes = document.querySelectorAll(".box"); // 모든 박스 선택

    boxes.forEach(box => {
        const tag = box.dataset.tag; // data-tag 속성에서 태그 가져오기
        if (tag.includes(input)) {
            box.classList.remove("hidden"); // 태그가 일치하면 보여줌
        } else {
            box.classList.add("hidden"); // 태그가 일치하지 않으면 숨김
        }
    });

    // 검색어가 비어 있으면 모든 박스를 다시 표시
    if (!input) {
        boxes.forEach(box => box.classList.remove("hidden"));
    }
});
