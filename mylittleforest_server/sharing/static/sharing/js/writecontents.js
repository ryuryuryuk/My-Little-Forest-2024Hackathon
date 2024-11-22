document.getElementById('image-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        const imageUrl = e.target.result;
        const previewImage = document.getElementById('uploaded-image');
        previewImage.src = imageUrl;
        document.getElementById('preview-img').style.display = 'block'; // 미리보기 표시
      };
      reader.readAsDataURL(file);
    }
  });

  // 게시글 추가 기능
document.getElementById('post-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('post-title').value;
    const content = document.getElementById('post-content').value;
    const imageInput = document.getElementById('image-upload');
    const imageFile = imageInput.files[0];

    // 이미지 파일이 있을 경우 처리 (이미지는 미리보기만 제공, 서버로 전송 기능은 포함되지 않음)
    if (imageFile) {
      console.log("업로드된 이미지 파일:", imageFile.name);
    }

    // 새 게시글을 처리하는 부분
    console.log("제목:", title);
    console.log("내용:", content);

    // 폼 초기화
    document.getElementById('post-title').value = '';
    document.getElementById('post-content').value = '';
    document.getElementById('image-upload').value = '';
    document.getElementById('preview-img').style.display = 'none'; // 미리보기 숨기기
  });
