from start.models import User  # start 앱에서 User 모델 임포트
from django.db import models

# 게시판 테이블
class Post_content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #저자
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField() # 본문
    image = models.ImageField(upload_to='content_images/')
    like_num = models.IntegerField(default=0, blank=True)  # 좋아요 개수
    scrap_num = models.IntegerField(default=0, blank=True)  # 스크랩 개수

    def __str__(self):
        return f"{self.title} by {self.author.nickname}"


# 댓글 테이블
class Comment(models.Model):
    post = models.ForeignKey(Post_content, on_delete=models.CASCADE, related_name='comments')  # 게시글 객체와 연결
    content = models.TextField()  # 댓글 내용
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자

    def __str__(self):
        return f"Comment by {self.commentor.nickname} on {self.post.title}"


# 스크랩 테이블
class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 스크랩한 사용자
    post = models.ForeignKey(Post_content, on_delete=models.CASCADE, related_name='scraps')  # 스크랩된 게시글 객체

    class Meta:
        unique_together = ('user', 'post')  # 중복 스크랩 방지

    def __str__(self):
        return f"{self.user.nickname} scrapped {self.post.title}"
