var selectedChoice = ""; // 사용자가 선택한 값을 저장할 변수
    
// 동작되는지 확인하려고 임시로 만든 함수
function selectChoice(button, choice) {
    // 다시 클릭하면 선택 해제
    if (button.classList.contains('selected')) {
        button.classList.remove('selected');
        selectedChoice = ""; // 선택 해제 시 변수 초기화
    } else {
        var buttons = document.querySelectorAll('.choice-button');
        buttons.forEach(function(button) {  // selected가 하나 뿐이어야 해서 forEach(반복) 돌고
            button.classList.remove('selected'); // 모든 버튼에서 selected 해제
        });
        button.classList.add('selected'); // 현재 버튼에만 selected 추가
        selectedChoice = choice; // 선택된 값 저장
    }

    var selectedButton = document.querySelector('.choice-button.selected');
    var nextButton = document.querySelector('.choice-next');
    nextButton.disabled = !selectedButton; // 선택이 없으면 '다음' 비활성화
}