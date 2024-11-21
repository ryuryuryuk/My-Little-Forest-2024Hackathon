function showConfirmText() {
    existingAlert = document.querySelector('.custom-alert');
    if (existingAlert) {
        existingAlert.remove();
    }

    alertBox = document.createElement('div');
    alertBox.classList.add('custom-alert');
    alertBox.innerHTML = `
        <p>'그룹 만들기'가 완료되었습니다. 화면을 확인해보세요.</p>
        <button onclick="goToNetworkingPage()">확인</button>
    `;
    document.body.appendChild(alertBox);
}

function goToNetworkingPage() {
    alertBox = document.querySelector('.custom-alert');
    if (alertBox) {
        alertBox.remove();
    }
    window.location.href = "networking.html";
}

/* 화면에 이미지 보여주기 */

function showImg(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const preview = document.getElementById('preview');
        preview.src = e.target.result;
        preview.style.display = 'block';
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}