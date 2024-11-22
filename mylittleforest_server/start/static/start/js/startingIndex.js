// 로고 이미지 요소 선택
const logo = document.getElementById('logo');

// 애니메이션 종료 이벤트 리스너 추가
logo.addEventListener('animationend', () => {
    // starting.html로 페이지 이동
    window.location.href = 'starting.html';
});
